# you have a list of usernames as below
import boto3
import io
client=boto3.client("iam")
usernames=["roni","john","mark"]

for username in usernames:
    client.create_user(UserName=username)
    client.create_login_profile(UserName=username,Password="Welcome@1234",PasswordResetRequired=False)
    response=client.create_access_key(UserName=username)
    access_key=response["AccessKey"]["AccessKeyId"]
    secret_access_key=response["AccessKey"]["SecretAccessKey"]

#create file
    with io.open(username+".txt","w",encoding="utf-8")as f1:
        f1.write(access_key+","+secret_access_key)
        f1.close()
    
#use the python list concept to create all 3 iam users together using python code