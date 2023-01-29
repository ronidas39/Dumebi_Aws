import boto3
import io

client=boto3.client("s3")

response=client.list_buckets()
buckets=response["Buckets"]
with io.open("output.csv","w",encoding="utf-8")as f1:
    f1.write("BucketName"+"\n")
    for bucket in buckets:
        f1.write(bucket["Name"]+"\n")
    f1.close()