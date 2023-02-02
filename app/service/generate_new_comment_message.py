from app.models.webhook import Webhook


async def generate_new_comment_issue_message(webhook: Webhook):
    message_text = f"[{webhook.repository.name}]({webhook.repository.homepage})\n\n" \
                   f"Появился новый комментарий для issue\n" \
                   f"[#{webhook.issue.iid} ''{webhook.issue.title}'']({webhook.issue.url})\n" \
                   f"Автор {webhook.user.username}:\n" \
                   f"[''{webhook.object_attributes.description}'']({webhook.object_attributes.url})"
    return message_text
