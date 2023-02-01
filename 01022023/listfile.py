import boto3
client=boto3.client("s3")
resource=boto3.resource("s3")
data=client.list_objects(Bucket="roni-jan29-test4")
files=data["Contents"]

for file in files:
    name=file["Key"]
    object=resource.Object("roni-jan29-test4",name)
    content=object.get()["Body"].read().decode("utf-8")
    print(content)
    print("=========================")