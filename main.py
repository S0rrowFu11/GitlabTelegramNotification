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


app = FastAPI()


@app.post("/WebHook/")
async def new_comment_webhook(web_hook_info: WebHook) -> WebHook:
    if web_hook_info.object_kind == "note" and web_hook_info.object_attributes.noteable_type == "Issue":
        message_text = await generate_new_comment_issue_message(web_hook_info)
        await send_message(message_text, web_hook_info)
        return web_hook_info
    if web_hook_info.object_kind == "note" and web_hook_info.object_attributes.noteable_type == "MergeRequest":
        message_text = await generate_new_comment_merge_message(web_hook_info)
        await send_message(message_text, web_hook_info)
        return web_hook_info
    if web_hook_info.object_kind == "issue":
        message_text = await generate_new_issue_message(web_hook_info)
        await send_message(message_text, web_hook_info)
        return web_hook_info
    if web_hook_info.object_kind == "merge_request":
        message_text = await generate_new_merge_request_message(web_hook_info)
        await send_message(message_text, web_hook_info)
        return web_hook_info
    if web_hook_info.object_kind == "pipeline":
        message_text = await generate_new_pipe_line_message(web_hook_info)
        await send_message(message_text, web_hook_info)
        return web_hook_info
    return web_hook_info
