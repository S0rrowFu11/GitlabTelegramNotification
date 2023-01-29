from Models.user import User
from Models.project import Project
from Models.build import Build
from Models.object_attributes import ObjectAttributes
from Models.repository import Repository
from Models.issue import Issue
from Models.assignee import Assignee
from Models.merge_request import MergeRequest
from typing import List
from pydantic import BaseModel


class WebHook(BaseModel):
    object_kind: str
    user: User
    project: Project
    object_attributes: ObjectAttributes
    repository: Repository | None = None
    issue: Issue | None = None
    builds: List[Build] = []
    assignees: List[Assignee] = []
    merge_request: MergeRequest | None = None
