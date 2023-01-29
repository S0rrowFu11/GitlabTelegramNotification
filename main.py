from typing import Union
from fastapi import FastAPI
from Service.send_message import send_message
import json
from Service.generate_new_pipe_line_message import generate_new_pipe_line_message
from Service.generate_new_comment_merge_message import generate_new_comment_merge_message
from Service.generate_new_comment_message import generate_new_comment_issue_message
from Service.generate_new_issue_message import generate_new_issue_message
from Service.generate_new_merge_request_message import generate_new_merge_request_message
from Models.webhook import WebHook
from Models.object_infos import ObjectInfos
from Service.get_telegram_ids import get_telegram_ids
app = FastAPI()
OBJECT_INFOS = ObjectInfos


@app.post("/WebHook/")
async def new_comment_webhook(web_hook_info: WebHook) -> WebHook:
    if web_hook_info.object_kind == OBJECT_INFOS.NOTE.value and web_hook_info.object_attributes.noteable_type == OBJECT_INFOS.ISSUE_NOTEABLE_TYPE.value:
        message_text = await generate_new_comment_issue_message(web_hook_info)
        ids = await get_telegram_ids(web_hook_info)
        await send_message(message_text, ids)
        return web_hook_info
    if web_hook_info.object_kind == OBJECT_INFOS.NOTE.value and web_hook_info.object_attributes.noteable_type == OBJECT_INFOS.MERGE_REQUEST_NOTEABLE_TYPE.value:
        message_text = await generate_new_comment_merge_message(web_hook_info)
        ids = await get_telegram_ids(web_hook_info)
        await send_message(message_text, ids)
        return web_hook_info
    if web_hook_info.object_kind == OBJECT_INFOS.ISSUE.value:
        message_text = await generate_new_issue_message(web_hook_info)
        ids = await get_telegram_ids(web_hook_info)
        await send_message(message_text, ids)
        return web_hook_info
    if web_hook_info.object_kind == OBJECT_INFOS.MERGE_REQUEST.value:
        message_text = await generate_new_merge_request_message(web_hook_info)
        ids = await get_telegram_ids(web_hook_info)
        await send_message(message_text, ids)
        return web_hook_info
    if web_hook_info.object_kind == OBJECT_INFOS.PIPELINE.value:
        message_text = await generate_new_pipe_line_message(web_hook_info)
        ids = await get_telegram_ids(web_hook_info)
        await send_message(message_text, ids)
        return web_hook_info
    return web_hook_info
