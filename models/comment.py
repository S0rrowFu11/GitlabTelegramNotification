from models.user import User
from models.project import Project
from models.object_attributes import Object_attributes
from models.repository import Repository
from models.issue import Issue
from pydantic import BaseModel


class CommentWebHook(BaseModel):
    object_kind: str
    event_type: str
    user: User
    project_id: int
    project: Project
    object_attributes: Object_attributes
    repository: Repository
    issue: Issue
