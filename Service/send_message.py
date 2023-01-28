from Models.webhook import WebHook


async def send_message(message_text: str, web_hook_info: WebHook):
    print(message_text)
