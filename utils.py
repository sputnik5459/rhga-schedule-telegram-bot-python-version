import pandas as pd
import requests as requests

import settings
from settings import XLSX_FILE_NAME


def load_xlsx() -> pd.DataFrame:
    if not XLSX_FILE_NAME:
        raise FileNotFoundError("Can not locate schedule xlsx. Check your 'settings.py'")
    df_file = pd.ExcelFile(f"{settings.PROJECT_ROOT}/{XLSX_FILE_NAME}")
    return pd.concat(
        [
            df_file.parse(
                sheet,
                skiprows=[0, 1],
                na_values=0,
                keep_default_na=False,
            ) for sheet in df_file.sheet_names[:-1]
        ],
        axis=0
    )


df = load_xlsx()


def parse_message(message: str) -> tuple[tuple, bool]:
    try:
        group, study_day = message.split(" ")
    except ValueError:
        return ("error", "Неверный формат запроса"), False
    # study_day = datetime.datetime.strptime(study_day, )
    return (group, study_day), True


def row_to_str(_df) -> str:
    res = ""
    for _, row in _df.iterrows():

        if not row['Дисциплина']:
            continue
        room = row['Аудитория/ссылка'] or row['Аудитория']
        if "http" in str(room):
            room = "Дистанционно"

        teacher = row['ФИО преподавателя'] or row['Преподаватель']

        res = res + (
            f"Время: {row['Время']}\n"
            f"Дисциплина: {row['Дисциплина']}\n"
            f"Вид занятий: {row['Вид занятий']}\n"
            f"ФИО преподавателя: {teacher}\n"
            f"Аудитория: {room}\n-\n"
        )
    return res if res else "В это день занятия для вашей группы не найдены"


def get_t_result(group: str, study_day: str) -> str:
    _df = df.loc[(df['Группа'] == group) & (df['Дата'] == study_day)]
    if _df.empty:
        return "К сожалению, по данному запросу ничего не найдено"
    return row_to_str(_df)


def set_new_webhook(url: str) -> dict:
    resp = requests.get(
        f"{settings.TELEGRAM_BOT_URL}setWebhook?"
        f"url={url}/webhook/"
    )
    resp.raise_for_status()
    resp_json = resp.json()
    return resp_json
