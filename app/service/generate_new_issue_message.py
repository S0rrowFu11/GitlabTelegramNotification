from app.models.webhook import Webhook


async def generate_new_issue_message(webhook: Webhook):
    if webhook.object_attributes.description is None:
        message_text = f"[{webhook.repository.name} notification.]({webhook.repository.homepage})\n" \
            f"Появился новый issue\n" \
            f"От пользователя {webhook.user.username}:\n" \
            f"[№{webhook.object_attributes.iid}\n" \
            f"{webhook.object_attributes.title}]({webhook.object_attributes.url})"
        return message_text
    else:
        message_text = f"[{webhook.repository.name} notification.]({webhook.repository.homepage})\n" \
                       f"Появился новый issue\n" \
                       f"[№{webhook.object_attributes.iid}\n" \
                       f"''{webhook.object_attributes.title}'']({webhook.object_attributes.url})\n" \
                       f"От пользователя {webhook.user.username}:\n" \
                       f"''{webhook.object_attributes.description}''"
        return message_text
