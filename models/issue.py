from pydantic import BaseModel


class Issue(BaseModel):
    author_id: int
    closed_at: str | None = None
    confidential: bool
    created_at: str
    description: str | None = None
    discussion_locked: str | None = None
    due_date: str | None = None
    id: int
    idd: int
    last_edited_at: str | None = None
    last_edited_by_id: int | None = None
    milestone_id: int | None = None
    moved_to_id: int | None = None
    duplicated_to_id: int | None = None
    project_id: int
    relative_position: int
    state_id: int
    time_estimate: int
    title: str | None = None
    updated_at: str | None = None
    updated_by_id: int | None = None
    url: str
    total_time_spent: int | None = None
    time_change: int | None = None
    human_total_time_spent: int | None = None
    human_time_change: int | None = None
    human_time_estimate: int | None = None
    assignee_ids: list[str] = []
    assignee_id: int | None = None
    labels: list[str] = []
    state: str
    severity: str
