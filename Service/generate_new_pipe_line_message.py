from Models.webhook import WebHook


async def generate_new_pipe_line_message(web_hook_info: WebHook):
    message_text = f"[{web_hook_info.repository.name}notification.]({web_hook_info.repository.homepage})\n" \
                   f"[Failed Pipeline {web_hook_info.object_attributes.id}]({web_hook_info.object_attributes.url})\n"
    for build in web_hook_info.builds:
        if build.status == "failed":
            message_text += build.name
            message_text += "\n"
    return message_text
