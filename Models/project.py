from pydantic import BaseModel


class Project(BaseModel):
    name: str | None = None
    web_url: str | None = None
