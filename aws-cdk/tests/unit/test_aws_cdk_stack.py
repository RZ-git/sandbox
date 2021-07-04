import json
import pytest

from aws_cdk import core
from aws-cdk.aws_cdk_stack import AwsCdkStack


def get_template():
    app = core.App()
    AwsCdkStack(app, "aws-cdk")
    return json.dumps(app.synth().get_stack("aws-cdk").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
