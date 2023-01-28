from pydantic import BaseModel


class MergeRequest(BaseModel):
    merge_status: str | None = None
    title: str | None = None
    web_url: str | None = None
    target_branch: str
    source_branch: str
    id: int | None = None
