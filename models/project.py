from pydantic import BaseModel


class Project(BaseModel):
    id: int
    name: str
    description: str | None = None
    web_url: str
    avatar_url: str | None = None
    git_ssh_url: str
    git_http_url: str
    namespace: str
    visibility_level: int
    path_with_namespace: str
    default_branch: str
    ci_config_path: str | None = None
    homepage: str
    url: str
    ssh_url: str
    http_url: str
