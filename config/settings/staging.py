# -*- coding: utf-8 -*-

from .base import *

DEBUG = False

'''
***********************
*   Force SSL/HTTPS   *
***********************
'''

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

'''
********************************
* PRODUCTION MIDDLEWARE ADDITION *
********************************
'''

MIDDLEWARE += [

]

'''
*******************
* DATABASE CONFIG *
*******************
'''

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<DB_NAME>',
        'USER': '<DB_USER>',
        'PASSWORD': '<DB_PASS>',
        'HOST': 'localhost',
        'PORT': '',
    }
}

'''
*************************
* DEVELOP APPS ADDITION *
*************************
'''

INSTALLED_APPS += [
    'guicorn',
]

'''
******************************
* TEMPLATES ADDITION SETTINGS *
******************************
'''

TEMPLATES[0]['OPTIONS']['context_processors'] += [

]

'''
*********************
* SYSTEM CONFIG *
*********************
'''

SITE_URL = 'https://api.simplestcode.com'

SENDING_EMAILS_ENABLED = True

"""
###################
# Logger Tracking #
###################
"""

sentry_sdk.init(
    dsn="https://326ef95239a2446b99c542cdfca7a5b4@o213835.ingest.sentry.io/5530095",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)