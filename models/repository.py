from pydantic import BaseModel


class Repository(BaseModel):
    name: str
    url: str
    description: str | None = None
    homepage: str
