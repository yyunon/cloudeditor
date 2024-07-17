from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

from .models.job import Job
from .models.video import Video
from .services.engine import Engine

app = FastAPI()

# @app.exception_handler(HTTPException)
# async def http_exception_handler(request, exc):
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)
# 
# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     return PlainTextResponse(str(exc), status_code=400)

@app.post("/create-video")
async def create_video(video: Video):
	status = {}
	for scene in video.scenes:
		status[scene.name]  = Engine() \
		.config(scene.media) \
		.process()
	return status

@app.get("/job-status")
async def create_video(job: Job):
	print(job)
	return {"message": "Hello World"}