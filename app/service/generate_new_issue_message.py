from app.models.webhook import Webhook


async def generate_new_issue_message(webhook: Webhook):
    message_text = f"[{webhook.repository.name}]({webhook.repository.homepage})\n\n" \
                   f"Появился новый issue\n" \
                   f"[#{webhook.object_attributes.iid}\n" \
                   f"''{webhook.object_attributes.title}'']({webhook.object_attributes.url})\n" \
                   f"Автор: {webhook.user.username}:\n" \
                   f"''{webhook.object_attributes.description}''"
    return message_text
