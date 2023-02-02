from fastapi import Request
from dotenv import load_dotenv
from app.utils.config import env_path, gitlab_secret


def is_access(request: Request):
    load_dotenv(env_path())
    gitlab_secret_token = gitlab_secret()

    if request.headers.get("X-Gitlab-Token") == gitlab_secret_token:
        return True

    return False
