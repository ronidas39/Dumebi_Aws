import boto3
client=boto3.client("iam")
client.delete_login_profile(UserName="john")
client.delete_access_key(UserName="john",AccessKeyId="AKIARA4HNYYVQ6CNRAAO")
client.delete_user(UserName="john")