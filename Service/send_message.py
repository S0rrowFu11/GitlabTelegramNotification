from Models.webhook import WebHook
import requests
import os
from dotenv import load_dotenv


async def send_message(message_text: str, ids: list[int]):
    load_dotenv(".env")
    token = os.environ.get("BOT_SECRET")
    for id in ids:
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data={"chat_id": id, "text": message_text, "parse_mode": "Markdown", "disable_web_page_preview": "true"})
