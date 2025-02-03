import pandas as pd

def explode_list_columns(df, output_csv=None):
    """
    Dynamically explodes all list-like columns in a DataFrame.
    
    - Handles empty lists by replacing them with blank values.
    - Identifies columns with list values automatically.
    - Explodes each list column sequentially.
    - Saves to CSV if `output_csv` is provided.

    :param df: Pandas DataFrame with possible list values.
    :param output_csv: (Optional) Path to save the output CSV file.
    :return: Processed DataFrame with exploded list values.
    """

    # Identify list-like columns and replace empty lists with [""] (blank)
    for col in df.columns:
        if df[col].apply(lambda x: isinstance(x, list)).any():
            df[col] = df[col].apply(lambda x: x if x else [""])  

    # Explode all identified list-like columns
    for col in df.columns:
        if df[col].apply(lambda x: isinstance(x, list)).any():
            df = df.explode(col)

    # Save to CSV if output file path is provided
    if output_csv:
        df.to_csv(output_csv, index=False)
    
    return df

# Sample Data
data = {
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Hobbies": [["Reading", "Swimming"], [], ["Music", "Gaming", "Cooking"]],
    "Scores": [[85, 90], [78, 80, 82], [88]]
}

df = pd.DataFrame(data)

# Process DataFrame
df_exploded = explode_list_columns(df, "output.csv")

# Print Output
print(df_exploded)
