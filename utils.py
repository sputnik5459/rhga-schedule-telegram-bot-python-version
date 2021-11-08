from typing import Optional, Union

import pandas as pd
import requests as requests

import settings
from settings import XLSX_FILE_NAME


def parse_message(message: str) -> Union[str, bool]:
    group, study_day = message.split(" ")


def format_df(df: pd.DataFrame) -> pd.DataFrame:
    return df


def load_xlsx() -> pd.DataFrame:
    if not XLSX_FILE_NAME:
        raise FileNotFoundError("Can not locate schedule xlsx. Check your 'settings.py'")
    return format_df(
        pd.read_excel(
            XLSX_FILE_NAME,
            skiprows=[0,1],
            na_values=0,
            keep_default_na=False,
            sheet_name="май21"
        )
    )


def parse_xlsx() -> dict:
    ...


def set_new_webhook(url: str) -> dict:
    resp = requests.get(
        f"{settings.TELEGRAM_BOT_URL}setWebhook?"
        f"url={url}/webhook/"
    )
    resp.raise_for_status()
    resp_json = resp.json()
    return resp_json
