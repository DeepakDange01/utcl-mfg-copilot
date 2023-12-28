import os
import json

# Get all environment variables
environment_variables = os.environ

# Convert to JSON format
json_data = json.dumps(dict(environment_variables), indent=2)

# Save the JSON data to a file
with open('environment_variables.json', 'w') as file:
    file.write(json_data)

print('Environment variables saved to environment_variables.json')
