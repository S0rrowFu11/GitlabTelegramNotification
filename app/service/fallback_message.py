def fallback_message(message: str | None, fallback="не указано"):
    if message is None or not message:
        return fallback
    else:
        return message
