## Config db for easy check-----
from pymongo import MongoClient

client = MongoClient(f"mongodb+srv://nizum:5kXPMsQBqhf65LZr@cluster0.4fphg1c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
vehicle_conn = client['Vehicle']
allocation_conn = client['Allocation']

## Best Way for config db------
# import os
# from pymongo import MongoClient
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# # Get USERNAMES and password from environment variables
# USERNAMES = os.getenv('USERNAMES')
# PASSWORD = os.getenv('PASSWORD')

# print('Loaded USERNAMES:', USERNAMES)  # Debug print
# print('Loaded PASSWORD:', PASSWORD)  # Debug print

# # Create MongoDB client using the environment variables
# if USERNAMES and PASSWORD:
#     client = MongoClient(f"mongodb+srv://{USERNAMES}:{PASSWORD}@cluster0.4fphg1c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#     vehicle_conn = client['Vehicle']
#     allocation_conn = client['Allocation']
#     print('MongoDB client created successfully.')
# else:
#     print('Error: USERNAMES or PASSWORD not loaded from .env file.')
