from pydantic import BaseModel
from typing import Optional

class Position(BaseModel):
	x: int
	y: int

class Dimensions(BaseModel):
	width: int
	height: int

class Media(BaseModel):
	name: Optional[str] = None
	type: Optional[str] = None
	source: Optional[str] = None
	duration: Optional[int] = None
	start_time: Optional[str] = None
	position: Optional[Position] = None
	dimensions: Optional[Dimensions] = None
	color: Optional[str] = None
	font_size: Optional[int] = None
	content: Optional[str] = None

class Scenes(BaseModel):
	name: Optional[str]
	start_time: Optional[str]
	end_time: Optional[str]
	media: list[Media] = set()
