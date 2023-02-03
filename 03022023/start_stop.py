import boto3,io
client=boto3.client("ec2")

with io.open("report.csv","r",encoding="utf-8") as f1:
    data=f1.read()
    f1.close()
lines=data.split("\n")[1:]
for line in lines:
    id=line.split(",")[0]
    state=line.split(",")[1]
    if state=="running":
        client.stop_instances(InstanceIds=[id])