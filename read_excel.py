import pandas as pd

# Load the Excel file
excel_file = pd.ExcelFile('your_file.xlsx')

# Initialize an empty list to store router names
router_names = []

# Iterate through each sheet in the Excel file
for sheet_name in excel_file.sheet_names:
    # Read the current sheet into a DataFrame
    df = excel_file.parse(sheet_name)
    
    # Get all columns containing 'Router' or 'router' in their name
    router_columns = [col for col in df.columns if 'Router' in col or 'router' in col]
    
    # Iterate through router columns and append unique router names to the list
    for col in router_columns:
        router_names.extend(df[col].unique())

# Remove any duplicate router names
router_names = list(set(router_names))

# Print the list of router names
print(router_names)
