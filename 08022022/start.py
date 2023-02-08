import boto3,io
client=boto3.client("ec2")
data=client.describe_instances()
instance_data=data["Reservations"]
for xx in instance_data:
    instances=xx["Instances"]
    for instance in instances:
        instance_id=instance["InstanceId"]
        state=instance["State"]["Name"]
        if state=="stopped":
            client.start_instances(InstanceIds=[instance_id])
