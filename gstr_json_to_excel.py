import os
import zipfile
import json
import pandas as pd
import tempfile

# Global lists for consolidation
consolidated_r1 = []
consolidated_r2a = []

def GSTR_R1_Convertor(json_file_path, excel_file_path, collect_consolidate=True):
    pos_map = {
        "20": "20-Jharkhand",
        # Add more POS codes if needed
    }
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    b2b_rows = []
    for party in data.get('b2b', []):
        ctin = party.get('ctin')
        for inv in party.get('inv', []):
            pos = inv.get('pos')
            pos_str = pos_map.get(pos, pos)
            for item in inv.get('itms', []):
                det = item.get('itm_det', {})
                row = {
                    "GSTIN/UIN of Recipient": ctin,
                    "Receiver Name": party.get('cname', ""),
                    "Invoice Number": inv.get('inum'),
                    "Invoice date": inv.get('idt'),
                    "Invoice Value": inv.get('val'),
                    "Place Of Supply": pos_str,
                    "Reverse Charge": inv.get('rchrg'),
                    "Invoice Type": inv.get('inv_typ'),
                    "E-Commerce GSTIN": inv.get('etin', ""),
                    "Item Number": item.get('num', ""),
                    "HSN/SAC": det.get('hsn_sc', ""),
                    "Description": det.get('desc', ""),
                    "Unit": det.get('uqc', ""),
                    "Quantity": det.get('qty', ""),
                    "Rate": det.get('rt', ""),
                    "Taxable Value": det.get('txval', ""),
                    "IGST Amount": det.get('iamt', ""),
                    "CGST Amount": det.get('camt', ""),
                    "SGST Amount": det.get('samt', ""),
                    "Cess Amount": det.get('csamt', ""),
                    "Total Tax": sum(float(det.get(k, 0) or 0) for k in ['iamt', 'camt', 'samt', 'csamt']),
                    "Document Type": inv.get('doctype', ""),
                    "Document Date": inv.get('docdt', ""),
                    "Document Number": inv.get('docnum', ""),
                    "Provisional Assessment": inv.get('pro_ass', ""),
                    "Diff Percent": det.get('diff_percent', ""),
                    "Supply Type": inv.get('sup_typ', ""),
                }
                b2b_rows.append(row)
    b2cs_rows = []
    for item in data.get('b2cs', []):
        det = item
        pos = item.get('pos')
        pos_str = pos_map.get(pos, pos)
        row = {
            "GSTIN/UIN of Recipient": "",
            "Receiver Name": "",
            "Invoice Number": "",
            "Invoice date": "",
            "Invoice Value": "",
            "Place Of Supply": pos_str,
            "Reverse Charge": "",
            "Invoice Type": "",
            "E-Commerce GSTIN": item.get('etin', ""),
            "Item Number": "",
            "HSN/SAC": det.get('hsn_sc', ""),
            "Description": det.get('desc', ""),
            "Unit": det.get('uqc', ""),
            "Quantity": det.get('qty', ""),
            "Rate": det.get('rt', ""),
            "Taxable Value": det.get('txval', ""),
            "IGST Amount": det.get('iamt', ""),
            "CGST Amount": det.get('camt', ""),
            "SGST Amount": det.get('samt', ""),
            "Cess Amount": det.get('csamt', ""),
            "Total Tax": sum(float(det.get(k, 0) or 0) for k in ['iamt', 'camt', 'samt', 'csamt']),
            "Document Type": item.get('doctype', ""),
            "Document Date": item.get('docdt', ""),
            "Document Number": item.get('docnum', ""),
            "Provisional Assessment": item.get('pro_ass', ""),
            "Diff Percent": det.get('diff_percent', ""),
            "Supply Type": item.get('sup_typ', ""),
        }
        b2cs_rows.append(row)
    df_b2b = pd.DataFrame(b2b_rows)
    df_b2cs = pd.DataFrame(b2cs_rows)
    with pd.ExcelWriter(excel_file_path) as writer:
        df_b2b.to_excel(writer, sheet_name="B2B", index=False)
        df_b2cs.to_excel(writer, sheet_name="B2CS", index=False)
    print(f"R1 Excel file '{excel_file_path}' created successfully.")
    if collect_consolidate:
        for row in b2b_rows:
            row['Type'] = 'B2B'
        for row in b2cs_rows:
            row['Type'] = 'B2CS'
        consolidated_r1.extend(b2b_rows + b2cs_rows)

def GSTR_R2A_Convertor(json_file_path, excel_file_path, collect_consolidate=True):
    pos_map = {
        "20": "20-Jharkhand",
        # Add more POS codes if needed
    }
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    b2b_rows = []
    for party in data.get('b2b', []):
        ctin = party.get('ctin')
        for inv in party.get('inv', []):
            pos = inv.get('pos')
            pos_str = pos_map.get(pos, pos)
            for item in inv.get('itms', []):
                det = item.get('itm_det', {})
                row = {
                    "GSTIN/UIN of Supplier": ctin,
                    "Supplier Name": party.get('cname', ""),
                    "Invoice Number": inv.get('inum'),
                    "Invoice date": inv.get('idt'),
                    "Invoice Value": inv.get('val'),
                    "Place Of Supply": pos_str,
                    "Reverse Charge": inv.get('rchrg'),
                    "Invoice Type": inv.get('inv_typ'),
                    "E-Commerce GSTIN": inv.get('etin', ""),
                    "Item Number": item.get('num', ""),
                    "HSN/SAC": det.get('hsn_sc', ""),
                    "Description": det.get('desc', ""),
                    "Unit": det.get('uqc', ""),
                    "Quantity": det.get('qty', ""),
                    "Rate": det.get('rt', ""),
                    "Taxable Value": det.get('txval', ""),
                    "IGST Amount": det.get('iamt', ""),
                    "CGST Amount": det.get('camt', ""),
                    "SGST Amount": det.get('samt', ""),
                    "Cess Amount": det.get('csamt', ""),
                    "Total Tax": sum(float(det.get(k, 0) or 0) for k in ['iamt', 'camt', 'samt', 'csamt']),
                    "Document Type": inv.get('doctype', ""),
                    "Document Date": inv.get('docdt', ""),
                    "Document Number": inv.get('docnum', ""),
                    "Provisional Assessment": inv.get('pro_ass', ""),
                    "Diff Percent": det.get('diff_percent', ""),
                    "Supply Type": inv.get('sup_typ', ""),
                }
                b2b_rows.append(row)
    b2cs_rows = []
    for item in data.get('b2cs', []):
        det = item
        pos = item.get('pos')
        pos_str = pos_map.get(pos, pos)
        row = {
            "GSTIN/UIN of Supplier": "",
            "Supplier Name": "",
            "Invoice Number": "",
            "Invoice date": "",
            "Invoice Value": "",
            "Place Of Supply": pos_str,
            "Reverse Charge": "",
            "Invoice Type": "",
            "E-Commerce GSTIN": item.get('etin', ""),
            "Item Number": "",
            "HSN/SAC": det.get('hsn_sc', ""),
            "Description": det.get('desc', ""),
            "Unit": det.get('uqc', ""),
            "Quantity": det.get('qty', ""),
            "Rate": det.get('rt', ""),
            "Taxable Value": det.get('txval', ""),
            "IGST Amount": det.get('iamt', ""),
            "CGST Amount": det.get('camt', ""),
            "SGST Amount": det.get('samt', ""),
            "Cess Amount": det.get('csamt', ""),
            "Total Tax": sum(float(det.get(k, 0) or 0) for k in ['iamt', 'camt', 'samt', 'csamt']),
            "Document Type": item.get('doctype', ""),
            "Document Date": item.get('docdt', ""),
            "Document Number": item.get('docnum', ""),
            "Provisional Assessment": item.get('pro_ass', ""),
            "Diff Percent": det.get('diff_percent', ""),
            "Supply Type": item.get('sup_typ', ""),
        }
        b2cs_rows.append(row)
    df_b2b = pd.DataFrame(b2b_rows)
    df_b2cs = pd.DataFrame(b2cs_rows)
    with pd.ExcelWriter(excel_file_path) as writer:
        df_b2b.to_excel(writer, sheet_name="B2B", index=False)
        df_b2cs.to_excel(writer, sheet_name="B2CS", index=False)
    print(f"R2A Excel file '{excel_file_path}' created successfully.")
    if collect_consolidate:
        for row in b2b_rows:
            row['Type'] = 'B2B'
        for row in b2cs_rows:
            row['Type'] = 'B2CS'
        consolidated_r2a.extend(b2b_rows + b2cs_rows)

# Add your process_source_dir, process_file, write_consolidated_reports, main, etc. here as needed.

def process_source_dir(source_dir, output_dir=None):
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        if filename.lower().endswith('.json') or filename.lower().endswith('.zip'):
            if '_r1_' in filename.lower():
                process_file(file_path, output_dir, GSTR_R1_Convertor)
            elif '_r2a_' in filename.lower():
                process_file(file_path, output_dir, GSTR_R2A_Convertor)

def process_file(file_path, output_dir, convertor_func):
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    excel_name = base_name + '.xlsx'
    excel_path = os.path.join(output_dir or os.path.dirname(file_path), excel_name)
    if file_path.lower().endswith('.json'):
        convertor_func(file_path, excel_path)
    elif file_path.lower().endswith('.zip'):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            for zip_info in zip_ref.infolist():
                if zip_info.filename.lower().endswith('.json'):
                    with tempfile.TemporaryDirectory() as tmpdirname:
                        extracted_path = os.path.join(tmpdirname, os.path.basename(zip_info.filename))
                        with open(extracted_path, 'wb') as f:
                            f.write(zip_ref.read(zip_info))
                        convertor_func(extracted_path, excel_path)
                    break

def write_consolidated_reports(output_dir):
    if consolidated_r1:
        df_r1 = pd.DataFrame(consolidated_r1)
        df_r1.to_excel(os.path.join(output_dir, "Consolidated_R1.xlsx"), index=False)
        print("Consolidated R1 Excel generated.")
    if consolidated_r2a:
        df_r2a = pd.DataFrame(consolidated_r2a)
        df_r2a.to_excel(os.path.join(output_dir, "Consolidated_R2A.xlsx"), index=False)
        print("Consolidated R2A Excel generated.")

if __name__ == "__main__":
    source_dir = input("Enter the source directory path (leave blank for current directory): ").strip()
    if not source_dir:
        source_dir = os.getcwd()
    output_dir = input("Enter the output directory path (leave blank to use source directory): ").strip()
    output_dir = output_dir if output_dir else source_dir
    process_source_dir(source_dir, output_dir)
    write_consolidated_reports(output_dir)
