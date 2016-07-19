import unittest
import boto3
import botocore
import os


REGION = 'ap-south-1'
BUCKET = 'km-sse-random137-kms'


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


    def test_put_object_with_s3_sse_kms_custom_cmk(self):
        kms_client = boto3.client('kms')
        response = kms_client.create_key()
        key_id = response['KeyMetadata']['KeyId']
        key_arn = response['KeyMetadata']['Arn']

        s3_client = boto3.client('s3')
        s3_client.put_object(
            Bucket = BUCKET,
            Key = 'polka-dot-jersey',
            Body = b'Sagan',
            ServerSideEncryption = 'aws:kms',
            SSEKMSKeyId = key_id
        )

        response = s3_client.get_object(
            Bucket = BUCKET,
            Key = 'polka-dot-jersey'
        )
        self.assertEqual('Sagan', response['Body'].read())

        response = kms_client.schedule_key_deletion(
            KeyId = key_id,
            PendingWindowInDays = 7
        )
        self.assertEqual(key_arn, response['KeyId'])


    def tearDown(self):
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(BUCKET)
        bucket.objects.delete()
        bucket.delete()


if __name__ == '__main__':
    unittest.main()
