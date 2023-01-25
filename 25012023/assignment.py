#create user with duplicate check , if user is available create the new user with 1 ,2,3 numberings
#john1
#john2


import boto3
client=boto3.client("iam")
try:
    client.get_user(UserName="john50")
    response="FOUND"
    # tags=response["User"]["Tags"]
    # for tag in tags:
    #    print(tag["Key"]+"="+tag["Value"])

except Exception as e:
    print(str(e))
    response="NOT_FOUND"

if response=="NOT_FOUND":
    #NORMAL CREATION
else:
    #1 ,2,3,4
    username="john50"+"1"

