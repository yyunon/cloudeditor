from pydantic import BaseModel

class Job(BaseModel):
	job_id: str
	status: str
	video_url: str