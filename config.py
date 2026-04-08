import os
from dotenv import load_dotenv

load_dotenv()

SERVICENOW_INSTANCE = os.getenv("SERVICENOW_INSTANCE")
SERVICENOW_ACCESS_TOKEN = os.getenv("SERVICENOW_ACCESS_TOKEN")