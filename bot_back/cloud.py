"""S3 functions for the Yandex S3"""

import json
from datetime import datetime
import boto3
from botocore.config import Config
from config.conf import CLOUD_S3_ID_KEY, CLOUD_S3_SECRET_KEY, BUCKET_NAME


s3 = boto3.client(
        aws_access_key_id=CLOUD_S3_ID_KEY,
        aws_secret_access_key=CLOUD_S3_SECRET_KEY,
        service_name='s3',
        endpoint_url='https://storage.yandexcloud.net',
        region_name='ru-central1',
        config=Config(signature_version='s3v4')
)


def save_food_entry_s3(food_dict: dict):
    """Upload food info to the S3 Cloud"""

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    entry = {
        'datetime': now,
        'description': food_dict.get("еда"),
        'калории': food_dict.get("калории"),
        'белки': food_dict.get("белки"),
        'жиры': food_dict.get("жиры"),
        'углеводы': food_dict.get("углеводы")
    }
    suffix = now.replace(':', '-').replace(' ', '_')
    filename = f"food_bot/{suffix}.json"
    print(filename)
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=filename,
        Body=json.dumps(entry,
                        ensure_ascii=False).encode('utf-8')
    )
