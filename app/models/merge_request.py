from pydantic import BaseModel


class MergeRequest(BaseModel):
    merge_status: str | None = None
    title: str | None = None
    web_url: str | None = None
    target_branch: str
    source_branch: str
    iid: int | None = None
    id: int | None = None
    assignee_ids: list[int] = []
    reviewer_ids: list[int] = []
