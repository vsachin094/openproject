import pandas as pd

# Create a DataFrame with column A
data = {'A': [1, 2, 3, 4, 5]}  # Example values for column A
df = pd.DataFrame(data)

# Function to generate three values based on input value
def generate_values(value):
    # Example logic to generate values
    value1 = value * 2
    value2 = value ** 2
    value3 = value + 10
    return value1, value2, value3

# Use apply method to create new columns
df[['B', 'C', 'D']] = df['A'].apply(lambda x: generate_values(x)).apply(pd.Series)

print(df)