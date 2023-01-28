from Models.webhook import WebHook


async def generate_new_merge_request_message(web_hook_info: WebHook):
    if web_hook_info.object_attributes.description is None:
        message_text = f"[{web_hook_info.repository.name} notification.]({web_hook_info.repository.homepage})\n" \
                       f"Появился новый merge request.\n" \
                       f"[№{web_hook_info.object_attributes.id} {web_hook_info.object_attributes.title}]({web_hook_info.object_attributes.url})\n" \
                       f"от пользователя {web_hook_info.user.username}\n" \
                       f"из ветки {web_hook_info.object_attributes.source_branch}\n" \
                       f"в ветку {web_hook_info.object_attributes.target_branch}"
        return message_text
    else:
        message_text = f"[{web_hook_info.repository.name} notification.]({web_hook_info.repository.homepage})\n" \
                       f"Появился новый merge request.\n" \
                       f"[№{web_hook_info.object_attributes.id} {web_hook_info.object_attributes.title}\n" \
                       f"{web_hook_info.object_attributes.description}]({web_hook_info.object_attributes.url})\n" \
                       f"от пользователя {web_hook_info.user.username}\n" \
                       f"из ветки {web_hook_info.object_attributes.source_branch}\n" \
                       f"в ветку {web_hook_info.object_attributes.target_branch}"
        return message_text
