from app.models.webhook import Webhook
from app.models.object_infos import ObjectType
OBJECT_INFOS = ObjectType


async def generate_new_pipe_line_message(webhook: Webhook):
    message_text = f"🛠 [{webhook.project.name}]({webhook.project.web_url})\n\n" \
                   f"Failed Pipeline #{webhook.object_attributes.id}:"
    for build in webhook.builds:
        if build.status == OBJECT_INFOS.FAILED_STATUS.value:
            message_text += f"\n\t - ***{build.name}***: {build.status}"
    return message_text
