from typing import Optional, TypeVar
import logging

_T = TypeVar("_T")

def set_context(logger, value):
	pass

class Logging:
	"""Logging mixin"""

	_log: logging.Logger | None = None

	_log_config_logger_name: Optional[str] = None

	_logger_name: Optional[str] = None
	
	def __init__(self, context=None):
		self._set_context(context)

	@staticmethod
	def _create_logger_name(
		logged_class: type[_T],
		log_config_logger_name: str | None = None,
		class_logger_name: str | None = None
	):
		logger_name: str = (
			class_logger_name
			if class_logger_name is not None
			else f"{logged_class.__module__}.{logged_class.__name__}"
		)
		if log_config_logger_name:
			return f"{log_config_logger_name}.{logger_name}" if logger_name else log_config_logger_name
		return logger_name
	
	@classmethod
	def _get_log(cls, obj: Any, classs: type[_T]) -> Logger:
		if obj._log is None: 
			logger_name: str = cls._create_logger_name(
				logged_class=classs,
				log_config_logger_name=obj._log_config_logger_name,
				class_logger_name=obj._logger_name
			)
			obj._log = logging.getLogger(logger_name)
		return obj._log
	
	@classmethod
	def logger(cls) -> Logger:
		return Logging._get_log(cls, cls)
	
	@property
	def log(self) -> Logger:
		return Logging._get_log(self, self.__class__)
	
	def _set_context(self, context):
		if context is not None:
			set_context(self.log, context)