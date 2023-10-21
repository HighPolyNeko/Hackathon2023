from dotenv import load_dotenv
import os


load_dotenv()

TG_TOKEN = os.environ.get("TG_TOKEN")
WEB_APP_URL = os.environ.get("WEB_APP_URL")
AUTH_URL = os.environ.get("AUTH_URL")
REG_URL = os.environ.get("REG_URL")
API_URL = os.environ.get("API_URL")
