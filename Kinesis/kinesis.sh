echo "Amazon Kinesis DataStream Command"

# 監視対象となるストリームを作成（ストリーム名はdemo-stream）
aws kinesis create-stream --stream-name demo-stream --shard-cuont 1

# 作成されたストリームを確認
aws kinesis list-stream
#{
#  "StreamNames": [
#    "demo-stream"
#  ]
#}
