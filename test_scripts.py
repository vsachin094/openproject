# {
#   "database": {
#     "host": "localhost",
#     "port": 3306,
#     "username": "user",
#     "password": "password123"
#   },
#   "api_key": "your_api_key_here"
# }

import os
import json

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Load configuration from file
config_file_path = os.path.join(script_dir, 'config.json')
with open(config_file_path, 'r') as f:
    _config = json.load(f)

# Accessible variables
DATABASE_HOST = _config['database']['host']
DATABASE_PORT = _config['database']['port']
DATABASE_USERNAME = _config['database']['username']
DATABASE_PASSWORD = _config['database']['password']
API_KEY = _config['api_key']
