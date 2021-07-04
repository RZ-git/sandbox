#!/usr/bin/env python3

from aws_cdk import core

from aws_cdk.aws_cdk_stack import AwsCdkStack


app = core.App()
AwsCdkStack(app, "aws-cdk")

app.synth()
