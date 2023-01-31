from app.models.webhook import Webhook


def _merge_request_description(description: str | None):
    if not description:
        return "не указано"
    return description


async def generate_new_merge_request_message(webhook: Webhook):
    message_text = f"[{webhook.repository.name}.]({webhook.repository.homepage})\n\n" \
        f"Появился новый merge request.\n" \
        f"[#{webhook.object_attributes.iid} {webhook.object_attributes.title}]({webhook.object_attributes.url})\n" \
        f"Описание: {_merge_request_description(webhook.object_attributes.description)}\n\n" \
        f"Автор {webhook.user.name}\n" \
        f"{webhook.object_attributes.source_branch} -> {webhook.object_attributes.target_branch}"
    return message_text
