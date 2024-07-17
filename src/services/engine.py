import os
import typing
import subprocess

from .bucket import download, upload
from ..models.scenes import Media

_T = typing.TypeVar("_T")

class Engine:
	_medias: list[typing.Any] = []

	def __init__(self):
		pass

	@classmethod
	def config(cls, medias: list[Media | None]) -> _T:
		for media in medias:
			download(media)
			cls._medias.append(media)
		return cls	

	@classmethod
	def process(cls) -> str:
		final_scene_files = []
		for scene in cls._medias:
			final_scene_files.append("-i")
			final_scene_files.append(scene.source)

		concat_filter = ''
		try:
			# Use ffmpeg to concatenate all processed files into the final video
			subprocess.run([
					'ffmpeg', '-safe', '-progress', '0', final_scene_files,
					'-filter_complex', concat_filter,
					'-c', 'copy', "out.mp4"
			])
		except subprocess.CalledProcessError as err:
			print(err.output)
    
		return "InProgress"