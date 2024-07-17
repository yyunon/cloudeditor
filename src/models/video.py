from pydantic import BaseModel
from .project import Project
from .scenes import Scenes

class Video(BaseModel):
	project: Project | None = None
	scenes: list[Scenes | None]  = set()
