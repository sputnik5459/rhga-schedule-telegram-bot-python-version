XLSX_FILE_NAME = "schedule.xlsx"

TELEGRAM_BOT_TOKEN = ""  # define in local_settings.py

try:
    from local_settings import *
except ImportError:
    raise FileNotFoundError

TELEGRAM_BOT_URL = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/'
