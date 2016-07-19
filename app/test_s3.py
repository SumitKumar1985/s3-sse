import unittest
import boto3
import botocore
import os

REGION = 'ap-south-1'
BUCKET = 'km-sse-random137'
SSE_KEY = os.urandom(32)


class TestS3(unittest.TestCase):

    def setUp(self):
        client = boto3.client('s3')
        try:
            client.head_bucket(
                Bucket = BUCKET,
            )
        except botocore.exceptions.ClientError as e:
            response = client.create_bucket(
                Bucket = BUCKET,
                CreateBucketConfiguration = {
                    'LocationConstraint': REGION
                }
            )

    def test_put_object_with_s3_sse_s3(self):
        client = boto3.client('s3')
        client.put_object(
            Bucket = BUCKET,
            Key = 'fangorn',
            Body = b'Treebeard',
            ServerSideEncryption = 'AES256'
        )

        response = client.get_object(
            Bucket = BUCKET,
            Key = 'fangorn'
        )
        self.assertEqual('Treebeard', response['Body'].read())


    def test_put_object_with_s3_sse_kms(self):
        client = boto3.client('s3')
        response = client.put_object(
            Bucket = BUCKET,
            Key = 'yellow-jersey',
            Body = b'Froome',
            ServerSideEncryption = 'aws:kms'
        )

        response = client.get_object(
            Bucket = BUCKET,
            Key = 'yellow-jersey'
        )
        self.assertEqual('Froome', response['Body'].read())


    def test_put_object_with_s3_sse_c(self):
        client = boto3.client('s3')
        client.put_object(
            Bucket = BUCKET,
            Key = 'baz',
            Body = b'foobar',
            SSECustomerKey = SSE_KEY,
            SSECustomerAlgorithm = 'AES256'
        )

        response = client.get_object(
            Bucket = BUCKET,
            Key = 'baz',
            SSECustomerKey = SSE_KEY,
            SSECustomerAlgorithm = 'AES256'
        )
        self.assertEqual('foobar', response['Body'].read())


    def tearDown(self):
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(BUCKET)
        bucket.objects.delete()
        bucket.delete()


if __name__ == '__main__':
    unittest.main()
