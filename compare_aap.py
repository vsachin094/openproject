import os
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def count_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return sum(1 for _ in f)
    except Exception as e:
        logging.error(f"Error reading {file_path}: {e}")
        return None

def extract_device_name(file_name):
    parts = file_name.split(".")
    if len(parts) >= 3:
        return parts[1]  # Extract device name from format xxxx.device_name.pre
    return "Unknown"

def find_matching_files(hpna_base_dirs, aap_base_dir, date, test_mappings):
    hpna_files = {}
    aap_files = {}
    
    for hpna_base_dir in hpna_base_dirs:
        logging.info(f"Processing base directory: {hpna_base_dir}")
        for aap_test, hpna_test in test_mappings.items():
            if not hpna_test:  # Skip if HPNA subdir is missing
                logging.info(f"Skipping AAP subdir {aap_test} as no matching HPNA subdir exists.")
                continue
            
            hpna_path = os.path.join(hpna_base_dir, date, hpna_test)
            aap_path = os.path.join(aap_base_dir, date, aap_test)
            logging.info(f"Processing subdir: HPNA={hpna_test}, AAP={aap_test}")
            
            if os.path.exists(hpna_path):
                for file in os.listdir(hpna_path):
                    if file.endswith(".pre"):  # HPNA diag file
                        device_name = extract_device_name(file)
                        hpna_files[(aap_test, file, device_name)] = os.path.join(hpna_path, file)
            
            if os.path.exists(aap_path):
                for file in os.listdir(aap_path):
                    device_name = extract_device_name(file)
                    aap_files[(aap_test, file, device_name)] = os.path.join(aap_path, file)
            
            logging.info(f"Completed processing subdir: HPNA={hpna_test}, AAP={aap_test}")
    
    return hpna_files, aap_files

def generate_comparison_reports(hpna_files, aap_files, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    subdir_data = {}
    unique_hpna_devices = {}
    unique_aap_devices = {}
    missing_devices = {}
    
    for (subdir, hpna_file, device_name), hpna_path in hpna_files.items():
        hpna_count = count_lines(hpna_path)
        aap_path = aap_files.get((subdir, hpna_file, device_name))
        aap_count = count_lines(aap_path) if aap_path else "N/A"
        flag = "Review Required" if aap_count != "N/A" and hpna_count != aap_count else "OK"
        
        unique_hpna_devices.setdefault(subdir, set()).add(device_name)
        if aap_path:
            unique_aap_devices.setdefault(subdir, set()).add(device_name)
        else:
            missing_devices.setdefault(subdir, set()).add(device_name)
        
        if subdir not in subdir_data:
            subdir_data[subdir] = []
        subdir_data[subdir].append([device_name, hpna_file, "Yes", "Yes" if aap_path else "No", hpna_count, aap_count, flag])
    
    for (subdir, aap_file, device_name), aap_path in aap_files.items():
        if subdir not in subdir_data:
            subdir_data[subdir] = []
        if not any(entry[1] == aap_file for entry in subdir_data[subdir]):
            aap_count = count_lines(aap_path)
            subdir_data[subdir].append([device_name, aap_file, "No", "Yes", "N/A", aap_count, "Review Required"])
            unique_aap_devices.setdefault(subdir, set()).add(device_name)
    
    for subdir, data in subdir_data.items():
        logging.info(f"Generating report for subdir: {subdir}")
        df = pd.DataFrame(data, columns=["Device Name", "Device File", "HPNA Found", "AAP Found", "HPNA Count", "AAP Count", "Flag"])
        output_csv = os.path.join(output_dir, f"comparison_report_{subdir}.csv")
        df.to_csv(output_csv, index=False)
        logging.info(f"Report generated: {output_csv}")
    
    for subdir in unique_hpna_devices.keys():
        logging.info(f"Subdir {subdir}: Unique devices in HPNA: {len(unique_hpna_devices.get(subdir, []))}")
        logging.info(f"Subdir {subdir}: Unique devices in AAP: {len(unique_aap_devices.get(subdir, []))}")
        logging.info(f"Subdir {subdir}: Devices missing in AAP: {len(missing_devices.get(subdir, []))}")

def main():
    hpna_base_dirs = ["/rfb_as", "/rfb_na", "/rfb_eu"]
    aap_base_dir = "aap_diags"
    date = "20250203"  # This can be dynamic
    test_mappings = {"test": "TEST", "ABC": "TEST1", "XYZ": "TEST3", "TEST4": ""}  # AAP to HPNA mapping
    output_dir = "comparison_reports"
    
    logging.info("Starting HPNA vs AAP comparison...")
    hpna_files, aap_files = find_matching_files(hpna_base_dirs, aap_base_dir, date, test_mappings)
    generate_comparison_reports(hpna_files, aap_files, output_dir)
    logging.info("Comparison process completed.")

if __name__ == "__main__":
    main()
