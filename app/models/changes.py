from pydantic import BaseModel
from created_at import CreatedAt


class Changes(BaseModel):
    created_at: CreatedAt | None = None

