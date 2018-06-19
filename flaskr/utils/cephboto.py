import boto
import boto.s3.connection
from boto.s3.key import Key
access_key = '3F7DPVAB2IJ0PNLOQHJN'
secret_key = 'Gw0gsUe8BVuS8H2bcH1jZEJBX4i1uRxyfhApqfzO'

conn = boto.connect_s3(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    host='127.0.0.1',
    port=37480,
    is_secure=False,  # uncomment if you are not using ssl
    calling_format=boto.s3.connection.OrdinaryCallingFormat(),
)


def save_file(keyname, file):
    bucket = conn.get_bucket('video-bucket', validate=False)
    if bucket is None:
        bucket = conn.create_bucket('video-bucket')
    k = Key(bucket)
    k.key = keyname
    size = k.set_contents_from_file(file)
    k.close()

    if size > 0:
        print('Save successfully')
        return True
    else:
        print('Save failing')
        return False

def get_file(keyname, filename):
    bucket = conn.get_bucket('video-bucket', validate=True)
    k = Key(bucket)
    k.key = keyname
    k.get_contents_to_filename(filename)
    k.close()
