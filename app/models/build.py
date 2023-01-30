from pydantic import BaseModel


class Build(BaseModel):
    name: str | None = None
    status: str | None = None
