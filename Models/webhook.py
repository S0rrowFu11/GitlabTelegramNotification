from Models.user import User
from Models.project import Project
from Models.build import Build
from Models.object_attributes import ObjectAttributes
from Models.repository import Repository
from Models.issue import Issue
from Models.assignee import Assignee
from Models.merge_request import MergeRequest
from pydantic import BaseModel


class WebHook(BaseModel):
    object_kind: str
    user: User
    project: Project
    object_attributes: ObjectAttributes
    repository: Repository
    issue: Issue | None = None
    builds: list[Build] = []
    assignees: list[Assignee] = []
    merge_request: MergeRequest | None = None
