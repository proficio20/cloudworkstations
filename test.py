#Function to create a GCS bucket
def create_bucket(bucket_name):
    try:
        storage_client = storage.Client()
        bucket = storage_client.create_bucket(bucket_name)
        print('Bucket {} created'.format(bucket.name))
    except Exception as e:
        print(e)

#Function to delete a GCS bucket
def delete_bucket(bucket_name):
    try:
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        bucket.delete()
        print('Bucket {} deleted'.format(bucket.name))
    except Exception as e:
        print(e)

#Function to list all GCS buckets
def list_buckets():
    try:
        storage_client = storage.Client()
        buckets = storage_client.list_buckets()
        for bucket in buckets:
            print(bucket.name)
    except Exception as e:
        print(e)

#Function to upload a file to a GCS bucket
def upload_file(bucket_name, source_file_name, destination_blob_name):
    try:
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)
        print('File {} uploaded to {}.'.format(source_file_name, destination_blob_name))
    except Exception as e:
        print(e)

#Function to download a file from a GCS bucket
def download_file(bucket_name, source_blob_name, destination_file_name):
    try:
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(source_blob_name)
        blob.download_to_filename(destination_file_name)
        print('File {} downloaded to {}.'.format(source_blob_name, destination_file_name))
    except Exception as e:
        print(e)

#Function to delete a file from a GCS bucket
def delete_file(bucket_name, blob_name):
    try:
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.delete()
        print('File {} deleted from {}.'.format(blob_name, bucket_name))
    except Exception as e:
        print(e)