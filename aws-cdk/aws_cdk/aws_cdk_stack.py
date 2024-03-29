from aws_cdk import (
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    core
)


class AwsCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self, "AwsCdkQueue",
            visibility_timeout=core.Duration.seconds(300),
        )

        topic = sns.Topic(
            self, "AwsCdkTopic"
        )

        topic.add_subscription(subs.SqsSubscription(queue))
