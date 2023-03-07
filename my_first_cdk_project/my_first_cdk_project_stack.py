from aws_cdk import (
    aws_s3 as s3,
    CfnOutput,
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
            versioned=False,
            encryption=s3.BucketEncryption.S3_MANAGED,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
        )

        my_bucket = s3.Bucket(
            self,
            "myBucketId1",
        )

        output_1 = CfnOutput(
            self,
            "myBucketOutput1",
            value=my_bucket.bucket_name,
            description="My first CDK Bucket",
            export_name="myBucketOutput1",
        )
