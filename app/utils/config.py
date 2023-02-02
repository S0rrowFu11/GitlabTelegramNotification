import os


def env_path() -> str:
    return ".env"


def dsn() -> str:
    return os.environ.get("DSN")


def gitlab_secret() -> str:
    return os.environ.get("GITLAB_SECRET")


def bot_secret() -> str:
    return os.environ.get("BOT_SECRET")
