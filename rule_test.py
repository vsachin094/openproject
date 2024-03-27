# Read rules from the text file
with open("rules.txt", "r") as file:
    rules = file.read()

# Example input dictionary
input_data = {
    "temperature": 25,  # Example temperature
    "humidity": 60      # Example humidity
}

# Execute the rules in the context of the input dictionary
exec(rules, input_data)

# The result variable will now hold the result according to the rules
print("Weather status:", input_data["result"])
