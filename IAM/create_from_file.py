import io
import boto3
client=boto3.client("iam")

with io.open("input.csv","r",encoding="utf-8")as f1:
    data=f1.read()
    f1.close()
lines=data.split("\n")[1:]
for line in lines:
    username=line.split(",")[0]
    password=line.split(",")[1]
    client.create_user(UserName=username)
    client.create_login_profile(UserName=username,Password="Welcome@1234",PasswordResetRequired=False)
    response=client.create_access_key(UserName=username)
    access_key=response["AccessKey"]["AccessKeyId"]
    secret_access_key=response["AccessKey"]["SecretAccessKey"]

#create file
    with io.open(username+".txt","w",encoding="utf-8")as f1:
        f1.write(access_key+","+secret_access_key)
        f1.close()