from app.models.webhook import Webhook
from dotenv import load_dotenv
from psycopg2 import connect
from app.models.object_infos import ObjectType
from typing import TypeVar, Iterable
from app.utils.config import dsn, env_path

OBJECT_INFOS = ObjectType

T = TypeVar("T")


def _extend_if_exists(*args: list[T]):
    target = []
    for arg in args:
        if isinstance(arg, Iterable):
            target.extend(arg)

    return target


async def _get_assignee_ids(webhook: Webhook):
    object_kind = webhook.object_kind
    if object_kind == OBJECT_INFOS.NOTE.value:
        note_type = webhook.object_attributes.noteable_type
        if note_type == OBJECT_INFOS.ISSUE_NOTEABLE_TYPE.value:
            return set(_extend_if_exists(webhook.object_attributes.author_id, webhook.issue.assignee_ids))
        elif note_type == OBJECT_INFOS.MERGE_REQUEST_NOTEABLE_TYPE.value:
            return set(_extend_if_exists([webhook.user.id], webhook.merge_request.assignee_ids, webhook.merge_request.reviewer_ids))
    elif object_kind == OBJECT_INFOS.ISSUE.value:
        return set(_extend_if_exists(webhook.object_attributes.assignee_ids, [webhook.object_attributes.author_id]))
    elif object_kind == OBJECT_INFOS.MERGE_REQUEST.value:
        return set(_extend_if_exists([webhook.user.id], webhook.object_attributes.assignee_ids, webhook.object_attributes.reviewer_ids))
    elif object_kind == OBJECT_INFOS.PIPELINE.value:
        return [webhook.user.id]


async def get_telegram_ids(webhook: Webhook):
    target_telegram_ids = []
    load_dotenv(env_path())
    connection = connect(dsn=dsn())
    cursor = connection.cursor()
    cursor.execute("""
    select telegram_id, gitlab_id from tg_gitlab.telegram_gitlab order by gitlab_id""")
    result = cursor.fetchall()
    for assingee_id in await _get_assignee_ids(webhook):
        for row in result:
            telegram_id, gitlab_id = row
            if assingee_id == gitlab_id:
                target_telegram_ids.append(telegram_id)

    if len(target_telegram_ids) > 0:
        return target_telegram_ids

    return [row[0] for row in result]
