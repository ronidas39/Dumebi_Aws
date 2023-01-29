import boto3
client=boto3.client("s3")
files=["names.csv","output.csv"]

for file in files:
    response=client.upload_file(file,"roni-jan29-test","upload_"+file)
    print(response)