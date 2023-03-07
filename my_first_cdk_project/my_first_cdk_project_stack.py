from aws_cdk import (
    aws_s3 as s3,
    Stack,
)
from constructs import Construct


class MyFirstCdkProjectStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        s3.Bucket(
            self,
            "myBucketId",
            bucket_name="tleonhafirstcdkproject",
            versioned=True,
            encryption=s3.BucketEncryption.KMS_MANAGED,
        )
