"""Loading the environment keys for the project"""

import os
from dotenv import load_dotenv


load_dotenv()


def get_checked_env(env_name):
    """Environment checker"""
    env = os.getenv(env_name)
    if not env:
        raise RuntimeError(f"The required variable isn't defined: {env_name}")
    return str(env)


OPENAI_TOKEN = get_checked_env('OPENAI_TOKEN')
BOT_TOKEN = get_checked_env('BOT_TOKEN')
ADMINS = get_checked_env('ADMINS')
CLOUD_S3_ID_KEY = str(os.getenv('CLOUD_S3_ID_KEY'))
CLOUD_S3_SECRET_KEY = str(os.getenv('CLOUD_S3_SECRET_KEY'))
BUCKET_NAME = str(os.getenv('BUCKET_NAME'))


admins_ids = [int(admin_id) for admin_id in ADMINS.split(',')]
