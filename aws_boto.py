import boto3
import os

# AWS_CREDS = {
#     'account_id': os.getenv("ACC_ID"),
#     'username': os.getenv("USERNAME"),
#     'password': os.getenv("PASS"),
#     'aws_access_key_id': os.getenv("AWS_ACCESS_KEY"),
#     'aws_secret_access_key': os.getenv("AWS_SECRET_ACCESS")
# }

aws_access_key_id = "AKIAWN3CAJ5MTA2LNR6J"
aws_secret_access_key = "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"


s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

s3.download_file("mb-cleanbucket", "sample_test2.json", "D:\panda_assignment\dump1.json")
