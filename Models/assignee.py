from pydantic import BaseModel


class Assignee(BaseModel):
    id: int | None = None
