import boto3
from datetime import datetime
import uuid


# API Document
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client.put_record


class KinesisStream:
    """ Kinesisストリームにデータを送信 """

    def put(self, request_times: int):
        kinesis = boto3.client('kinesis')
        stream_name = 'demo-stream'
        data = datetime.utcnow().strftime('%s')
        partition_key = str(uuid.uuid4())

        # アラームを発生させるのに必要な任意の件数分書き込み処理を行う。
        for i in range(request_times):
            kinesis.put_record(
                StreamName=stream_name,
                Data=data,
                PartitionKey=partition_key
            )


# 例）１分間に10回以上の書き込み時アラームが発生なら15回など。
KinesisStream().put(15)
