import boto3
import io

client=boto3.client("iam")



with io.open("input.csv","r",encoding="utf-8")as f1:
    data=f1.read()
    f1.close()

lines=data.split("\n")[1:]

for line in lines:
        try:
            username=line.split(",")[0]
            response=client.create_user(UserName=username)
            print(response)
        except Exception as e:
            print(str(e))