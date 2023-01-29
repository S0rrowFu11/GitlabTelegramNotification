from pydantic import BaseModel
from typing import List


class MergeRequest(BaseModel):
    merge_status: str | None = None
    title: str | None = None
    web_url: str | None = None
    target_branch: str
    source_branch: str
    iid: int | None = None
    id: int | None = None
    assignee_ids: List[int] = []
    reviewer_ids: List[int] = []
