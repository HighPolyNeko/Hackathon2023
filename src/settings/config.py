from dotenv import load_dotenv
import os


load_dotenv()

TG_TOKEN = os.environ.get("TG_TOKEN")
WEB_APP_URL = os.environ.get("WEB_APP_URL")
AUTH_URL = os.environ.get("AUTH_URL")
