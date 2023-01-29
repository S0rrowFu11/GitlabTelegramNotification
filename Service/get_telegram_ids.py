from Models.webhook import WebHook
import os
from dotenv import load_dotenv
from psycopg2 import OperationalError, connect
from Models.object_infos import ObjectInfos
OBJECT_INFOS = ObjectInfos


async def get_telegram_ids(webhook_info: WebHook):
    ids = []
    all_ids = []
    load_dotenv(".env")
    connection = connect(
        database=os.environ.get("DATABASE"),
        user=os.environ.get("USER"),
        password=os.environ.get("PASSWORD"),
        host=os.environ.get("HOST"),
        port=os.environ.get("PORT"),
    )
    cursor = connection.cursor()
    cursor.execute("""
    select telegram_id, gitlab_id from tg_gitlab.telegram_gitlab order by gitlab_id""")
    result = cursor.fetchall()
    for row in result:
        all_ids.append(row[0])
    if webhook_info.object_kind == OBJECT_INFOS.NOTE.value and webhook_info.object_attributes.noteable_type == OBJECT_INFOS.ISSUE_NOTEABLE_TYPE.value:
        for assignee_id in webhook_info.issue.assignee_ids:
            for row in result:
                telegram_id = row[0]
                gitlab_id = row[1]
                if assignee_id == gitlab_id:
                    ids.append(telegram_id)
        if len(ids) > 0:
            return ids
        else:
            return all_ids
    if webhook_info.object_kind == OBJECT_INFOS.NOTE.value and webhook_info.object_attributes.noteable_type == OBJECT_INFOS.MERGE_REQUEST_NOTEABLE_TYPE.value:
        for assignee_id in webhook_info.merge_request.assignee_ids:
            for row in result:
                telegram_id = row[0]
                gitlab_id = row[1]
                if assignee_id == gitlab_id:
                    ids.append(telegram_id)
        for reviewer_id in webhook_info.merge_request.reviewer_ids:
            for row in result:
                telegram_id = row[0]
                gitlab_id = row[1]
                if reviewer_id == gitlab_id:
                    ids.append(telegram_id)
        if len(ids) > 0:
            return ids
        else:
            return all_ids
    if webhook_info.object_kind == OBJECT_INFOS.ISSUE.value or webhook_info.object_kind == OBJECT_INFOS.MERGE_REQUEST.value:
        for assignee_id in webhook_info.object_attributes.assignee_ids:
            for row in result:
                telegram_id = row[0]
                gitlab_id = row[1]
                if assignee_id == gitlab_id:
                    ids.append(telegram_id)
        if webhook_info.object_kind == OBJECT_INFOS.MERGE_REQUEST.value:
            for reviewer_id in webhook_info.object_attributes.reviewer_ids:
                for row in result:
                    telegram_id = row[0]
                    gitlab_id = row[1]
                    if reviewer_id == gitlab_id:
                        ids.append(telegram_id)
        if len(ids) > 0:
            return ids
        else:
            return all_ids
    if webhook_info.object_kind == OBJECT_INFOS.PIPELINE.value:
        assignee_id = webhook_info.user.id
        for row in result:
            telegram_id = row[0]
            gitlab_id = row[1]
            if assignee_id == gitlab_id:
                ids.append(telegram_id)
        if len(ids) > 0:
            return ids
        else:
            return all_ids
