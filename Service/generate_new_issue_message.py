from Models.webhook import WebHook


async def generate_new_issue_message(web_hook_info: WebHook):
    if web_hook_info.object_attributes.description is None:
        message_text = f"[{web_hook_info.repository.name} notification.]({web_hook_info.repository.homepage})\n" \
                   f"Появился новый issue\n" \
                   f"От пользователя {web_hook_info.user.username}:\n" \
                   f"[№{web_hook_info.object_attributes.iid}\n" \
                   f"{web_hook_info.object_attributes.title}]({web_hook_info.object_attributes.url})"
        return message_text
    else:
        message_text = f"[{web_hook_info.repository.name} notification.]({web_hook_info.repository.homepage})\n" \
                       f"Появился новый issue\n" \
                       f"[№{web_hook_info.object_attributes.iid}\n" \
                       f"''{web_hook_info.object_attributes.title}'']({web_hook_info.object_attributes.url})\n" \
                       f"От пользователя {web_hook_info.user.username}:\n" \
                       f"''{web_hook_info.object_attributes.description}''"
        return message_text
