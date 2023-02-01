import boto3
resource=boto3.resource("s3")

object=resource.Object("roni-jan29-test4","input.csv")
content=object.get()["Body"].read().decode("utf-8")
print(content)

