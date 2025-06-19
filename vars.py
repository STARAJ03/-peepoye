# DON'T add anything here just add in render's secret or env section 
from os import environ

API_ID = int(environ.get("API_ID", "27765349"))
API_HASH = environ.get("API_HASH", "9df1f705c8047ac0d723b29069a1332b")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
