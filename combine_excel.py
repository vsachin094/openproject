import pandas as pd
import glob

# Specify the path to the directory containing the Excel files
path = 'your_directory_path/*.xlsx'

# Use glob to get a list of file names that match the pattern
all_files = glob.glob(path)

# Create an empty list to store the combined data
combined_data = []

# Iterate through each file in the list
for filename in all_files:
    # Read each Excel file into a pandas ExcelFile object
    xls = pd.ExcelFile(filename)
    # Iterate through each sheet in the Excel file
    for sheet_name in xls.sheet_names:
        # Read each sheet into a pandas DataFrame
        df = pd.read_excel(xls, sheet_name=sheet_name)
        # Append the DataFrame to the list
        combined_data.append(df)

# Concatenate all DataFrames in the list into one
final_df = pd.concat(combined_data, ignore_index=True)

# Write the combined DataFrame to a new Excel file
final_df.to_excel('combined_data.xlsx', index=False)