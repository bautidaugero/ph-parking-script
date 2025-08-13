import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_BASE_URL = os.environ.get('API_BASE_URL') 
    API_USERNAME = os.environ.get('API_USERNAME') 
    API_PASSWORD = os.environ.get('API_PASSWORD') 
    GROUP_ID = int(os.environ.get('GROUP_ID', 16)) # Demo: 16, Prod: 9
    GROUP_NAME = os.environ.get('GROUP_NAME') or 'CABLE 2'  # Demo: CABLE 2, Prod: Parking PH