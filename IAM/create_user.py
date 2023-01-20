import boto3
client=boto3.client("iam")
import io

#user creation
client.create_user(UserName="mark",Tags=[
    {
        "Key":"Department",
        "Value":"IT"
    }

])
client.create_login_profile(UserName="mark",Password="Welcome@1234",PasswordResetRequired=False)
response=client.create_access_key(UserName="mark")
access_key=response["AccessKey"]["AccessKeyId"]
secret_access_key=response["AccessKey"]["SecretAccessKey"]

#create file
with io.open("output.txt","w",encoding="utf-8")as f1:
    f1.write(access_key+","+secret_access_key)
    f1.close()


    
