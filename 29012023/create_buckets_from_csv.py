import io,boto3

client=boto3.client("s3")

with io.open("names.csv","r",encoding="utf-8")as f1:
    data=f1.read()
    f1.close()
lines=data.split("\n")[1:]

for line in lines:
    response=client.create_bucket(Bucket=line)
    print(response)
    