import json
def lambda_handler(event, context):
    # TODO implement
    bucket=event["Records"][0]["s3"]["bucket"]["name"]
    file=event["Records"][0]["s3"]["object"]["key"]
    print(bucket,file)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
