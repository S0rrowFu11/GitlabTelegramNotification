from app.models.webhook import Webhook
import requests
import os
from dotenv import load_dotenv
from app.utils.config import env_path, bot_secret
from loguru import logger
import logging


async def send_message(message_text: str, ids: list[int]):
    # logging.basicConfig()
    # logging.getLogger().setLevel(logging.DEBUG)
    # requests_log = logging.getLogger("requests.packages.urllib3")
    # requests_log.setLevel(logging.DEBUG)
    # requests_log.propagate = True
    try:
        load_dotenv(env_path())
        token = bot_secret()
        test = "TEST"
        #https://api.telegram.org/bot{token}/sendMessage
        for id in ids:
            response = requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data={
                "chat_id": id, "text": f"", "parse_mode": "Markdown", "disable_web_page_preview": "true"})
            response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        logger.error(err)
