from .base import *

DEBUG = True

CORS_ORIGIN_REGEX_WHITELIST = ('^(https?://)?localhost|0\.0\.0\.0(:[0-9]{4})?$', )

try:
	from .local import *
except ImportError:
	pass
