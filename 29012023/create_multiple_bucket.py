import boto3

client=boto3.client("s3")

names=["roni-jan29-test1","roni-jan29-test2","roni-jan29-test3"]

for name in names:
    response=client.create_bucket(Bucket=name)
    print(response)
