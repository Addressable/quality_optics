import boto3


class S3Utils:
    def __init__(self, bucket_name: str):
        self._bucket_name = bucket_name

        self._s3_resource = None
        self._s3_client = None
        self._bucket = None

        self.connect()

    def connect(self):
        print(f"connecting to {self._bucket_name}")
        self._s3_resource = boto3.resource('s3')
        self._s3_client = boto3.client('s3')
        self._bucket = self._s3_resource.Bucket(self._bucket_name)

    def write_file(self, file_path: str, destination_key: str):
        self._bucket.upload_file(file_path, destination_key)

    def write_files(self, files: dict):
        for file in files:
            self.write_file(file['file_path'], file['destination_key'])

    def list(self, prefix:str = ''):
        return self._s3_client.list_objects(self._bucket_name, MaxKey=100, Prefix=prefix)

