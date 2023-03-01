from pydantic import BaseModel


class CreatedAt(BaseModel):
    previous: str | None = None
    current: str | None = None
