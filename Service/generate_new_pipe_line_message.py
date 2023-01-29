from Models.webhook import WebHook
from Models.object_infos import ObjectInfos
OBJECT_INFOS = ObjectInfos


async def generate_new_pipe_line_message(web_hook_info: WebHook):
    message_text = f"[{web_hook_info.project.name} notification.]({web_hook_info.project.web_url})\n" \
                   f"Failed Pipeline №{web_hook_info.object_attributes.iid}:"
    for build in web_hook_info.builds:
        if build.status == OBJECT_INFOS.FAILED_STATUS.value:
            message_text += f"\n{build.name} status: {build.status}"
    return message_text
