import unittest
import boto3
import botocore

BUCKET = 'km-sse-random137'

class TestS3(unittest.TestCase):

    def setUp(self):
        client = boto3.client('s3')
        try:
            client.head_bucket(
                Bucket = BUCKET
            )
        except botocore.exceptions.ClientError as e:
            response = client.create_bucket(
                Bucket = BUCKET
            )


    def test_put_object_with_sse(self):
        client = boto3.client('s3')
        response = client.get_bucket_location(
            Bucket = BUCKET
        )
        self.assertEqual(None, response['LocationConstraint'])


    def tearDown(self):
        client = boto3.client('s3')
        client.delete_bucket(
            Bucket = BUCKET
        )


if __name__ == '__main__':
    unittest.main()
