from pydantic import BaseModel
from typing import List


class ObjectAttributes(BaseModel):
    author_id: int | None
    id: int | None = None
    iid: int | None = None
    title: str | None = None
    description: str | None = None
    url: str | None = None
    status: str | None = None
    source_branch: str | None = None
    target_branch: str | None = None
    assignee_ids: List[int] = []
    reviewer_ids: List[int] = []
    noteable_type: str | None = None
