import pandas as pd

def explode_list_columns(df, output_csv=None):
    """
    Dynamically explodes all list-like columns in a DataFrame.
    
    - Handles mixed data types (lists + strings/integers).
    - Converts empty lists to blank values ("").
    - Explodes each list column sequentially.
    - Saves to CSV if `output_csv` is provided.

    :param df: Pandas DataFrame with possible list values.
    :param output_csv: (Optional) Path to save the output CSV file.
    :return: Processed DataFrame with exploded list values.
    """

    # Identify columns that contain lists
    for col in df.columns:
        if df[col].apply(lambda x: isinstance(x, list)).any():
            # Ensure non-list values remain unchanged, empty lists become [""]
            df[col] = df[col].apply(lambda x: x if isinstance(x, list) else [x] if pd.notna(x) else [""])
    
    # Explode all detected list-like columns
    for col in df.columns:
        if df[col].apply(lambda x: isinstance(x, list)).any():
            df = df.explode(col)
    
    # Replace NaN values with empty strings
    df = df.fillna("")

    # Save to CSV if output file path is provided
    if output_csv:
        df.to_csv(output_csv, index=False)

    return df

# Sample Data with Mixed Types
data = {
    "ID": [1, 2, 3, 4],
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Hobbies": [["Reading", "Swimming"], [], ["Music", "Gaming", "Cooking"], None],
    "Scores": [[85, 90], [78, 80, 82], [88], "Pass"]
}

df = pd.DataFrame(data)

# Process DataFrame
df_exploded = explode_list_columns(df, "output.csv")

# Print Output
print(df_exploded)
