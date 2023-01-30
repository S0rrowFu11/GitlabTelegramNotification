from app.models.webhook import Webhook


async def generate_new_comment_issue_message(webhook: Webhook):
    if webhook.issue.title is None:
        message_text = f"[{webhook.repository.name} notification.]({webhook.repository.homepage})\n" \
            f"Появился новый комментарий для issue\n" \
            f"[№{webhook.issue.iid}]({webhook.issue.url})\n" \
            f"От пользователя {webhook.user.username}:\n" \
            f"[''{webhook.object_attributes.description}'']({webhook.object_attributes.url})"
        return message_text
    else:
        message_text = f"[{webhook.repository.name} notification.]({webhook.repository.homepage})\n" \
                       f"Появился новый комментарий для issue\n" \
                       f"[№{webhook.issue.iid} ''{webhook.issue.title}'']({webhook.issue.url})\n" \
                       f"От пользователя {webhook.user.username}:\n" \
                       f"[''{webhook.object_attributes.description}'']({webhook.object_attributes.url})"
        return message_text
