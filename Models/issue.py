from pydantic import BaseModel


class Issue(BaseModel):
    author_id: int | None = None
    id: int | None = None
    title: str | None = None
    url: str | None = None

