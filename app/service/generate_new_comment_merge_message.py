from app.models.webhook import Webhook


async def generate_new_comment_merge_message(webhook: Webhook):
    if webhook.merge_request.title is None:
        message_text = f"[{webhook.repository.name} notification.]({webhook.repository.homepage})\n" \
                       f"Появился новый комментарий для merge request\n" \
                       f"[№{webhook.merge_request.iid}]({webhook.merge_request.web_url})\n" \
                       f"из {webhook.merge_request.source_branch}\n" \
                       f"в {webhook.merge_request.target_branch}\n"\
                       f"От пользователя {webhook.user.name}:\n" \
                       f"[''{webhook.object_attributes.description}'']({webhook.object_attributes.url})"
        return message_text
    else:
        message_text = f"[{webhook.repository.name} notification.]({webhook.repository.homepage})\n" \
                       f"Появился новый комментарий для merge request\n" \
                       f"[№{webhook.merge_request.iid} ''{webhook.merge_request.title}'']({webhook.merge_request.web_url})\n" \
                       f"из {webhook.merge_request.source_branch}\n" \
                       f"в {webhook.merge_request.target_branch}\n" \
                       f"От пользователя {webhook.user.name}:\n" \
                       f"[''{webhook.object_attributes.description}'']({webhook.object_attributes.url})"
        return message_text
