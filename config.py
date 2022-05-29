import os

from dotenv import load_dotenv

load_dotenv()  # Loads .env file

API_ID = os.getenv('API_ID')  # API ID
API_HASH = os.getenv('API_HASH')  # API HASH
