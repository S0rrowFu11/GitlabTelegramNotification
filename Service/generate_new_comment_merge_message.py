from Models.webhook import WebHook


async def generate_new_comment_merge_message(web_hook_info : WebHook):
    if web_hook_info.merge_request.title is None:
        message_text = f"[{web_hook_info.repository.name} notification.]({web_hook_info.repository.homepage})\n" \
                       f"Появился новый комментарий для merge request\n" \
                       f"[№{web_hook_info.merge_request.id}]({web_hook_info.merge_request.web_url})\n" \
                       f"из {web_hook_info.merge_request.source_branch}\n" \
                       f"в {web_hook_info.merge_request.target_branch}\n"\
                       f"От пользователя {web_hook_info.user.name}:\n" \
                       f"[{web_hook_info.object_attributes.description}]({web_hook_info.object_attributes.url})"
        return message_text
    else:
        message_text = f"[{web_hook_info.repository.name} notification.]({web_hook_info.repository.homepage})\n" \
                       f"Появился новый комментарий для merge request\n" \
                       f"[№{web_hook_info.merge_request.id} {web_hook_info.merge_request.title}]({web_hook_info.merge_request.web_url})\n" \
                       f"из {web_hook_info.merge_request.source_branch}\n" \
                       f"в {web_hook_info.merge_request.target_branch}\n" \
                       f"От пользователя {web_hook_info.user.name}:\n" \
                       f"[{web_hook_info.object_attributes.description}]({web_hook_info.object_attributes.url})"
        return message_text
