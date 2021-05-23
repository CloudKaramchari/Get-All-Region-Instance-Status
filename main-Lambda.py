import json
import boto3

regionBoto = boto3.client('ec2')
response = regionBoto.describe_regions()['Regions']

def lambda_handler(event, context):
    i = 0
    regions=response
    all_region = [region['RegionName'] for region in regions]
    while i < len(all_region):
         j = all_region[i]
         ec2 = boto3.resource('ec2',region_name=j)
         print("Region", "Instance-ID", "Instance-Type", "Instance-Status")
         instances = ec2.instances.filter()
         for instance in instances:
           print(j, instance.id, instance.instance_type, instance.state['Name'])
         i += 1
