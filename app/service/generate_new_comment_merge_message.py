from app.models.webhook import Webhook


async def generate_new_comment_merge_message(webhook: Webhook):
    message_text = f"💡 [{webhook.repository.name}]({webhook.repository.homepage})\n\n" \
                   f"Появился новый комментарий\n" \
                   f"[#{webhook.merge_request.iid} ''{webhook.merge_request.title}'']({webhook.merge_request.web_url})\n" \
                   f"{webhook.merge_request.source_branch} -> {webhook.merge_request.target_branch}\n" \
                   f"Автор: {webhook.user.name}:\n" \
                   f"[''{webhook.object_attributes.description}'']({webhook.object_attributes.url})"
    return message_text
