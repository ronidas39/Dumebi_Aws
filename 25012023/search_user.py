import boto3
client=boto3.client("iam")
try:
    client.get_user(UserName="john50")
    response="FOUND"
    tags=response["User"]["Tags"]
    for tag in tags:
       print(tag["Key"]+"="+tag["Value"])


except Exception as e:
    print(str(e))
