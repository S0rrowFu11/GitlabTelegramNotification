from pydantic import BaseModel


class ObjectAttributes(BaseModel):
    author_id: int
    id: int | None
    title: str | None = None
    description: str | None = None
    url: str | None = None
    status: str | None = None
    source_branch: str | None = None
    target_branch: str | None = None
    assignment_ids: list[int] = []
    noteable_type: str | None = None
