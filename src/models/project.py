from pydantic import BaseModel

class Output(BaseModel):
	format: str
	resolution: str

class Project(BaseModel):
	name: str
	output: Output
