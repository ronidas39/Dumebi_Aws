import boto3,io
client=boto3.client("ec2")
data=client.describe_instances()
instance_data=data["Reservations"]
with io.open("report.csv","w",encoding="utf-8") as f1:
    f1.write("ID,STATE"+"\n")
    for xx in instance_data:
        instances=xx["Instances"]
        for instance in instances:
            f1.write(instance["InstanceId"]+","+instance["State"]["Name"]+"\n")
    f1.close()
        