from fastapi import FastAPI
from app.service.send_message import send_message
import json
from app.service.generate_new_pipe_line_message import generate_new_pipe_line_message
from app.service.generate_new_comment_merge_message import generate_new_comment_merge_message
from app.service.generate_new_comment_message import generate_new_comment_issue_message
from app.service.generate_new_issue_message import generate_new_issue_message
from app.service.generate_new_merge_request_message import generate_new_merge_request_message
from app.models.webhook import Webhook
from app.models.object_infos import ObjectType
from app.service.get_telegram_ids import get_telegram_ids


app = FastAPI()
OBJECT_INFOS = ObjectType


@app.post("/Webhook/")
async def new_comment_webhook(webhook: Webhook) -> Webhook:
    print(webhook)
    object_kind = webhook.object_kind
    ids = await get_telegram_ids(webhook)

    if object_kind == OBJECT_INFOS.NOTE.value:
        note_type = webhook.object_attributes.noteable_type

        if note_type == OBJECT_INFOS.ISSUE_NOTEABLE_TYPE.value:
            message_text = await generate_new_comment_issue_message(webhook)
            await send_message(message_text, ids)
            return webhook
        elif note_type == OBJECT_INFOS.MERGE_REQUEST_NOTEABLE_TYPE.value:
            message_text = await generate_new_comment_merge_message(webhook)
            await send_message(message_text, ids)
            return webhook

    elif object_kind == OBJECT_INFOS.ISSUE.value:
        message_text = await generate_new_issue_message(webhook)
        await send_message(message_text, ids)
        return webhook
    elif object_kind == OBJECT_INFOS.MERGE_REQUEST.value:
        message_text = await generate_new_merge_request_message(webhook)
        await send_message(message_text, ids)
        return webhook
    elif object_kind == OBJECT_INFOS.PIPELINE.value:
        message_text = await generate_new_pipe_line_message(webhook)
        await send_message(message_text, ids)
        return webhook

    return webhook
