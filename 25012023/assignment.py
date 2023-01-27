#create user with duplicate check , if user is available create the new user with 1 ,2,3 numberings
#john1
#john2

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
        client.get_user(UserName=username)
        response="FOUND"
        for i in range(1,100):
            modified_username=username+str(i)
            try:
                client.get_user(UserName=modified_username)
            except Exception as e:
                print(str(e))
                response="NOT_FOUND"
                username=modified_username
                break


    except Exception as e:
        print(str(e)+", hence this user is a new user")
        response="NOT_FOUND"
        username=username
        


    if response=="NOT_FOUND":
        client.create_user(UserName=username)
        print(username)
  
    else:
        client.create_user(UserName=username)
        print(username)


