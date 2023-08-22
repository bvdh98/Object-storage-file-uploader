import os
from minio import Minio
from minio.error import S3Error
from dotenv import load_dotenv
# load environment variables
load_dotenv()
# get environment variables
BUCKET = os.getenv('BUCKET')
ACCESS_KEY = os.getenv('ACCESS_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')
OBJECT_STORAGE_SERVER = os.getenv('OBJECT_STORAGE_SERVER')
# ENTER the name of the object
OBJECT = ""
# ENTER the file path of the document you want to upload
FILE = ""


def main():
    # Create a client with the object storage server, its access key
    # and secret key.
    client = Minio(
        OBJECT_STORAGE_SERVER,
        access_key=ACCESS_KEY,
        secret_key=SECRET_KEY,
    )
    # Make bucket if it doesn't exist.
    found = client.bucket_exists(BUCKET)
    if not found:
        client.make_bucket(BUCKET)
    else:
        print(f"Bucket {BUCKET} already exists")

    # Upload the file as the specified object to the bucket
    client.fput_object(
        BUCKET, OBJECT, FILE,
    )
    print(
        "'{}' is successfully uploaded as "
        "object '{}' to bucket '{}'.".format(FILE, OBJECT, BUCKET)
    )


if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)
