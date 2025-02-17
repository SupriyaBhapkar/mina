import logging
import datetime
import os

class BaseConfig(object):
    DEBUG = False
    LOGGING_LEVEL = logging.INFO
    LOGGING_LOCATION = str(os.environ['LOGGING_LOCATION']).strip()

    POSTGRES_HOST = str(os.environ['POSTGRES_HOST']).strip()
    POSTGRES_PORT = int(os.environ['POSTGRES_PORT'])
    POSTGRES_USER = str(os.environ['POSTGRES_USER']).strip()
    POSTGRES_PASSWORD = str(os.environ['POSTGRES_PASSWORD']).strip()
    POSTGRES_DB = str(os.environ['POSTGRES_DB']).strip()

    CREDENTIAL_PATH = str(os.environ['CREDENTIAL_PATH']).strip()
    GCS_BUCKET_NAME = str(os.environ['GCS_BUCKET_NAME']).strip()
    PROVIDER_ACCOUNT_PUB_KEYS_FILE = str(os.environ['PROVIDER_ACCOUNT_PUB_KEYS_FILE']).strip()
    SURVEY_INTERVAL_MINUTES = int(os.environ['SURVEY_INTERVAL_MINUTES'])
    UPTIME_DAYS_FOR_SCORE = int(os.environ['UPTIME_DAYS_FOR_SCORE'])
    FROM_EMAIL = str(os.environ['FROM_EMAIL']).strip()
    TO_EMAILS = str(os.environ['TO_EMAILS']).strip()
    SUBJECT = str(os.environ['SUBJECT']).strip()
    PLAIN_TEXT = str(os.environ['PLAIN_TEXT']).strip()
    SENDGRID_API_KEY = str(os.environ['SENDGRID_API_KEY']).strip()
    SPREADSHEET_SCOPE = str(os.environ['SPREADSHEET_SCOPE']).strip()
    SPREADSHEET_NAME = str(os.environ['SPREADSHEET_NAME']).strip()
    SPREADSHEET_JSON = str(os.environ['SPREADSHEET_JSON']).strip()
    MAX_THREADS_TO_DOWNLOAD_FILES= str(os.environ['MAX_THREADS_TO_DOWNLOAD_FILES']).strip()