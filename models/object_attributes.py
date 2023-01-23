from pydantic import BaseModel


class Object_attributes(BaseModel):
    attachment: str | None = None
    author_id: int
    change_position: str | None = None #may be not str, TBC
    commit_id: int | None = None
    created_at: str
    discussion_id: str
    id: int
    line_code: str | None = None #may be not str, TBC
    note: str
    noteable_id: int
    noteable_type: str
    original_position: str | None = None #may be not str, TBC
    position: str | None = None #may be not str, TBC
    project_id: int
    resolved_at: str | None = None #may be not str, TBC
    resolved_by_id: int | None = None #may be not str, TBC
    resolved_by_push: str | None = None #may be not str, TBC
    st_diff: str | None = None #may be not str, TBC
    system: bool
    type: str | None = None
    updated_at: str
    updated_by_id: int
    description: str
    url: str
