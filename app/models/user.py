from pydantic import BaseModel


class User(BaseModel):
    id: int | None = None
    name: str | None = None
    username: str | None = None
    avatar_url: str | None = None
    email: str | None = None
