from app.models.user import User
from app.models.project import Project
from app.models.build import Build
from app.models.object_attributes import ObjectAttributes
from app.models.repository import Repository
from app.models.issue import Issue
from app.models.assignee import Assignee
from app.models.merge_request import MergeRequest
from pydantic import BaseModel
from app.models.changes import Changes


class Webhook(BaseModel):
    object_kind: str
    user: User
    project: Project
    object_attributes: ObjectAttributes
    repository: Repository | None = None
    issue: Issue | None = None
    builds: list[Build] = []
    merge_request: MergeRequest | None = None
    changes: Changes | None = None
