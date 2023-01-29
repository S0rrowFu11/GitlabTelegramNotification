from pydantic import BaseModel


class Repository(BaseModel):
    name: str | None = None
    homepage: str | None = None
