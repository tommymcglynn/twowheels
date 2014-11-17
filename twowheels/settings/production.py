from .base import *
import os

DEBUG = False

CORS_ORIGIN_REGEX_WHITELIST = ('^(https?://)?twowheels-env-([a-z_0-9]*)\.elasticbeanstalk\.com$',
                               '^(https?://)?(www\.)?twowheel\.in')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': os.environ['RDS_USERNAME'],
        'PASSWORD': os.environ['RDS_PASSWORD'],
        'HOST': os.environ['RDS_HOSTNAME'],  # Set to empty string for localhost.
        'PORT': os.environ['RDS_PORT'],  # Set to empty string for default.
        'CONN_MAX_AGE': 600,  # number of seconds database connections should persist for
    }
}

try:
	from .local import *
except ImportError:
	pass
