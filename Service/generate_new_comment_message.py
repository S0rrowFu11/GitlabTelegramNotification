from Models.webhook import WebHook


async def generate_new_comment_issue_message(web_hook_info: WebHook):
    if web_hook_info.issue.title is None:
        message_text = f"[{web_hook_info.repository.name} notification.]({web_hook_info.repository.homepage})\n" \
                   f"Появился новый комментарий для issue\n" \
                   f"[№{web_hook_info.issue.iid}]({web_hook_info.issue.url})\n" \
                   f"От пользователя {web_hook_info.user.username}:\n" \
                   f"[''{web_hook_info.object_attributes.description}'']({web_hook_info.object_attributes.url})"
        return message_text
    else:
        message_text = f"[{web_hook_info.repository.name} notification.]({web_hook_info.repository.homepage})\n" \
                       f"Появился новый комментарий для issue\n" \
                       f"[№{web_hook_info.issue.iid} ''{web_hook_info.issue.title}'']({web_hook_info.issue.url})\n" \
                       f"От пользователя {web_hook_info.user.username}:\n" \
                       f"[''{web_hook_info.object_attributes.description}'']({web_hook_info.object_attributes.url})"
        return message_text
