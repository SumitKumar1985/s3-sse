import unittest
import boto3

class TestS3(unittest.TestCase):

    def setUp(self):
        client = boto3.client('s3')
        response = client.create_bucket(
            Bucket='km-sse-random137'
        )

    def test_save_file(self):
        client = boto3.client('s3')
        response = client.get_bucket_location(
            Bucket='km-sse-random137'
        )
        self.assertEqual(None, response['LocationConstraint'])


    def tearDown(self):
        client = boto3.client('s3')
        response = client.delete_bucket(
            Bucket='km-sse-random137'
        )


if __name__ == '__main__':
    unittest.main()
