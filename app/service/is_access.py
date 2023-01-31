import os
from fastapi import Request
from dotenv import load_dotenv


def is_access(request: Request):
    load_dotenv(".env")
    gitlab_secret = os.environ.get("GITLAB_SECRET")

    if request.headers.get("X-Gitlab-Token") == gitlab_secret:
        return True

    return False
