"""
Django settings for csp project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import logging
from datetime import timedelta

import dj_database_url
import dj_redis_url
import django
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v1*ah#)@vyov!7c@n&c2^-*=8d)-d!u9@#c4o*@k=1(1!jul6&'
HASHID_KEY = 'ho(f%5a9dl_*)(*h2n6v#&yk5+mbc8u58uhlbexoqkj@d)0h6='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', False)

TEMPLATE_DEBUG = DEBUG
APPEND_SLASH = True

# Allow all host headers
ALLOWED_HOSTS = ['*']
PRODUCTION_HOSTS = ['daemo.herokuapp.com', 'daemo.stanford.edu']

REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',),
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        # 'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        # 'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope'}
}
ACCESS_TOKEN_EXPIRE_SECONDS = 604800
OAUTH2_PROVIDER_APPLICATION_MODEL = 'oauth2_provider.Application'
OAUTH2_PROVIDER_ACCESS_TOKEN_MODEL = 'oauth2_provider.AccessToken'
MIGRATION_MODULES = {
    'oauth2_provider': 'crowdsourcing.migrations.oauth2_provider',
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.sessions',
    'django.contrib.postgres',
    'oauth2_provider',
    'corsheaders',
    'compressor',
    'crispy_forms',
    'rest_framework',
    'ws4redis',
    'crowdsourcing',
    'mturk'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'crowdsourcing.middleware.active.CustomActiveViewMiddleware',
    'crowdsourcing.middleware.requirement.RequirementMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'csp.urls'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'static/django_templates'), os.path.join(BASE_DIR, 'static/mturk')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'ws4redis.context_processors.default',
            ]
        },
    },
]

WSGI_APPLICATION = 'csp.wsgi.application'

DATABASES = {
    'default': dj_database_url.config()
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

# Email
EMAIL_HOST = 'localhost'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_ENABLED = True
EMAIL_SENDER = 'daemo@cs.stanford.edu'
EMAIL_SENDER_DEV = ''
EMAIL_SENDER_PASSWORD_DEV = ''
EMAIL_BACKEND = "crowdsourcing.backends.sendgrid_backend.SendGridBackend"
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY', '')

# Email messages
EMAIL_NOTIFICATIONS_INTERVAL = os.environ.get('EMAIL_NOTIFICATIONS_INTERVAL', 30)

# Others
GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
}

if float(django.get_version()[0:3]) < 1.8:
    FIXTURE_DIRS = (
        os.path.join(BASE_DIR, 'fixtures')
    )

# Stripe
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY', '')
STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY', '')

REGISTRATION_ALLOWED = os.environ.get('REGISTRATION_ALLOWED', False)
PASSWORD_RESET_ALLOWED = True

LOGIN_URL = '/login'
USERNAME_MAX_LENGTH = 30

# CORS
CORS_ORIGIN_ALLOW_ALL = True
# Use only to restrict to specific servers/domains

# CORS_ORIGIN_WHITELIST = (
#     'stanford-qa.com',
# )

CORS_URLS_REGEX = r'^/api/done/*$'
CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'OPTIONS'
)

HALF_OFF = True
NON_PROFIT_EMAILS = ['.edu', '.org']

SITE_HOST = os.environ.get('SITE_HOST', 'https://daemo.org')

REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')
REDIS_CONNECTION = dj_redis_url.parse(REDIS_URL)

DISCOURSE_API_KEY = os.environ.get('DISCOURSE_API_KEY', '')
DISCOURSE_BASE_URL = os.environ.get('DISCOURSE_BASE_URL', 'https://forum.daemo.org')
DISCOURSE_SSO_SECRET = os.environ.get('DISCOURSE_SSO_SECRET', 'ku_&j@77ghe6%-6788fg)^dmc4f((jx)w=o!q%+h!teydc7zes')
DISCOURSE_TOPIC_TASKS = os.environ.get('DISCOURSE_TOPIC_TASKS', None)
if DISCOURSE_TOPIC_TASKS is not None:
    DISCOURSE_TOPIC_TASKS = int(DISCOURSE_TOPIC_TASKS)

MAX_TASKS_IN_PROGRESS = int(os.environ.get('MAX_TASKS_IN_PROGRESS', 8))

# Task Expiration
TASK_EXPIRATION_BEAT = os.environ.get('TASK_EXPIRATION_BEAT', 1)

DEFAULT_TASK_TIMEOUT = timedelta(hours=os.environ.get('DEFAULT_TASK_TIMEOUT', 8))

# MTurk
MTURK_CLIENT_ID = os.environ.get('MTURK_CLIENT_ID', 'INVALID')
MTURK_CLIENT_SECRET = os.environ.get('MTURK_CLIENT_SECRET', 'INVALID')
MTURK_HOST = os.environ.get('MTURK_HOST', 'mechanicalturk.sandbox.amazonaws.com')
MTURK_WORKER_HOST = os.environ.get('MTURK_WORKER_HOST', 'https://workersandbox.mturk.com/mturk/externalSubmit')
ID_HASH_MIN_LENGTH = 8
MTURK_WORKER_USERNAME = 'mturk'
MTURK_QUALIFICATIONS = os.environ.get('MTURK_QUALIFICATIONS', True)
MTURK_BEAT = os.environ.get('MTURK_BEAT', 1)
AWS_DAEMO_KEY = os.environ.get('AWS_DAEMO_KEY')
MTURK_ONLY = os.environ.get('MTURK_ONLY', False)
MTURK_COMPLETION_TIME = int(os.environ.get('MTURK_COMPLETION_TIME', 12))
MTURK_THRESHOLD = 0.61
POST_TO_MTURK = os.environ.get('POST_TO_MTURK', True)
MTURK_SYS_QUALIFICATIONS = os.environ.get('MTURK_SYS_QUALIFICATIONS', True)

WORKER_SPLIT_PERCENT = float(os.environ.get('WORKER_SPLIT_PERCENTILE', 0.75))

# AWS
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', 'daemo')
AWS_S3_FILE_OVERWRITE = False

# Celery
BROKER_URL = REDIS_URL
BROKER_POOL_LIMIT = None
CELERY_RESULT_BACKEND = REDIS_URL
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'America/Los_Angeles'

FEED_BOOMERANG = 1

BOOMERANG_MIDPOINT = 1.99
BOOMERANG_MAX = 3.0
BOOMERANG_WORKERS_NEEDED = int(os.environ.get('BOOMERANG_WORKERS_NEEDED', 15))
HEART_BEAT_BOOMERANG = int(os.environ.get('HEART_BEAT_BOOMERANG', 5))
BOOMERANG_LAMBDA = float(os.environ.get('BOOMERANG_LAMBDA', 0.6))
BOOMERANG_TASK_ALPHA = float(os.environ.get('BOOMERANG_TASK_ALPHA', 0.3))
BOOMERANG_REQUESTER_ALPHA = float(os.environ.get('BOOMERANG_REQUESTER_ALPHA', 0.4))
BOOMERANG_PLATFORM_ALPHA = float(os.environ.get('BOOMERANG_PLATFORM_ALPHA', 0.5))
MIN_RATINGS_REQUIRED = 5

COLLECTIVE_REJECTION_THRESHOLD = 7

IS_SANDBOX = os.environ.get('SANDBOX', 'False') == 'True'
DAEMO_FIRST = True
AUTO_APPROVE_FREQ = os.environ.get('AUTO_APPROVE_FREQ', 8)  # hours
EXPIRE_RETURNED_TASKS = os.environ.get('EXPIRE_RETURNED_TASKS', 2)  # days

# Sessions
SESSION_ENGINE = 'redis_sessions.session'
SESSION_REDIS_HOST = REDIS_CONNECTION['HOST']
SESSION_REDIS_PORT = REDIS_CONNECTION['PORT']
SESSION_REDIS_DB = REDIS_CONNECTION['DB']
SESSION_REDIS_PASSWORD = REDIS_CONNECTION['PASSWORD']
SESSION_REDIS_PREFIX = 'session'

# Web-sockets
WS4REDIS_CONNECTION = {
    'host': REDIS_CONNECTION['HOST'],
    'port': REDIS_CONNECTION['PORT'],
    'db': REDIS_CONNECTION['DB'],
    'password': REDIS_CONNECTION['PASSWORD'],
}
WEBSOCKET_URL = '/ws/'
WS4REDIS_EXPIRE = 1800
# WS4REDIS_HEARTBEAT = '--heartbeat--'
WS4REDIS_PREFIX = 'ws'
WS_API_URLS = ['/ws/bot']

# Payments (Stripe)
DAEMO_WORKER_PAY = timedelta(minutes=int(os.environ.get('DAEMO_WORKER_PAY', 60)))
DAEMO_CHARGEBACK_FEE = 0.005
STRIPE_CHARGE_LIFETIME = timedelta(days=90)

from utils import ws4redis_process_request

WS4REDIS_PROCESS_REQUEST = ws4redis_process_request

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ("Daemo", 'daemo@cs.stanford.edu'),  # add more team members
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
SERVER_EMAIL = 'daemo@cs.stanford.edu'

CELERY_REDIS_MAX_CONNECTIONS = 10
CELERY_IGNORE_RESULT = True
CELERY_STORE_ERRORS_EVEN_IF_IGNORED = True
MIN_WORKERS_FOR_STATS = 10

# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        },
        'suppress_deprecated': {
            '()': 'csp.settings.SuppressDeprecated'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false', 'suppress_deprecated'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True
        },
        'console': {
            'level': 'INFO',
            'filters': ['suppress_deprecated'],
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'py.warnings': {
            'handlers': ['console'],
        },
    }
}


class SuppressDeprecated(logging.Filter):
    def filter(self, record):
        warnings = [
            'RemovedInDjango18Warning',
            'RemovedInDjango19Warning',
            'RemovedInDjango110Warning:',
        ]

        # Return false to suppress message.
        return not any([warn in record.getMessage() for warn in warnings])


PYTHON_VERSION = 2
try:
    from local_settings import *
except Exception as e:
    if DEBUG:
        print e.message

CELERYBEAT_SCHEDULE = {
    # 'mturk-push-tasks': {
    #     'task': 'mturk.tasks.mturk_publish',
    #     'schedule': timedelta(minutes=int(MTURK_BEAT)),
    # },
    'pay-workers': {
        'task': 'crowdsourcing.tasks.pay_workers',
        'schedule': DAEMO_WORKER_PAY,
    },
    # 'expire-hits': {
    #     'task': 'mturk.tasks.expire_hits',
    #     'schedule': timedelta(minutes=int(TASK_EXPIRATION_BEAT)),
    # },
    'expire-tasks': {
        'task': 'crowdsourcing.tasks.expire_tasks',
        'schedule': timedelta(minutes=int(TASK_EXPIRATION_BEAT)),
    },
    'auto-approve-tasks': {
        'task': 'crowdsourcing.tasks.auto_approve_tasks',
        'schedule': timedelta(minutes=4),
    },
    'email-notifications': {
        'task': 'crowdsourcing.tasks.email_notifications',
        'schedule': timedelta(minutes=int(EMAIL_NOTIFICATIONS_INTERVAL)),
    },
    'update-feed-boomerang': {
        'task': 'crowdsourcing.tasks.update_feed_boomerang',
        'schedule': timedelta(minutes=HEART_BEAT_BOOMERANG),
    }
}

# Secure Settings
if not DEBUG:
    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    # SECURE_HSTS_SECONDS = 31536000
    # SECURE_HSTS_INCLUDE_SUBDOMAINS = False
    SECURE_FRAME_DENY = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SECURE_SSL_REDIRECT = True
    CSRF_TRUSTED_ORIGINS = [
        'daemo.herokuapp.com', 'daemo.stanford.edu',
        'daemo-staging.herokuapp.com', 'daemo-staging.stanford.edu',
        'daemo.org', 'www.daemo.org', 'daemo-test.herokuapp.com'
    ]

REQUIRED_CONFIGS = ['AWS_DAEMO_KEY', 'AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY', 'STRIPE_SECRET_KEY',
                    'STRIPE_PUBLIC_KEY', 'SITE_HOST']

for config in REQUIRED_CONFIGS:
    if config not in locals() and config not in globals():
        print("Required configuration parameter is missing: {}".format(config))
        exit(-1)
