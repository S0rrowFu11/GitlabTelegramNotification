from pydantic import BaseModel
from typing import List


class Issue(BaseModel):
    author_id: int | None = None
    id: int | None = None
    iid: int | None = None
    title: str | None = None
    url: str | None = None
    assignee_ids: List[int] = []
