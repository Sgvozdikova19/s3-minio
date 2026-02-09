import boto3
from botocore.exceptions import ClientError
import os

# Настройки подключения к MinIO
s3_client = boto3.client(
    's3',
    endpoint_url='http://localhost:9000',
    aws_access_key_id='minioadmin',
    aws_secret_access_key='minioadmin',
    region_name='us-east-1'
)

BUCKET_NAME = 'homework-bucket'
FILE_NAME = 'test-file.txt'
OBJECT_NAME = 'uploaded-test-file.txt'

def main():
    print("=== Работа с S3 (MinIO) через Python ===\n")

    # 1. Создать бакет
    try:
        s3_client.create_bucket(Bucket=BUCKET_NAME)
        print(f"Бакет '{BUCKET_NAME}' создан.")
    except ClientError as e:
        if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
            print(f"Бакет '{BUCKET_NAME}' уже существует.")
        else:
            raise

    # 2. Загрузить файл
    try:
        s3_client.upload_file(FILE_NAME, BUCKET_NAME, OBJECT_NAME)
        print(f"Файл '{FILE_NAME}' успешно загружен как '{OBJECT_NAME}'.")
    except Exception as e:
        print(f"Ошибка загрузки: {e}")

    # 3. Получить список файлов в бакете
    print("\nСписок файлов в бакете:")
    try:
        response = s3_client.list_objects_v2(Bucket=BUCKET_NAME)
        if 'Contents' in response:
            for obj in response['Contents']:
                print(f" - {obj['Key']} (размер: {obj['Size']} байт)")
        else:
            print("Бакет пустой.")
    except Exception as e:
        print(f"Ошибка получения списка: {e}")

if __name__ == "__main__":
    main()


import webbrowser
webbrowser.open('http://localhost:9001/buckets/homework-bucket/browse')