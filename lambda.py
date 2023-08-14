import boto3
import re

def lambda_handler(event, context):
    instance_id = event['detail']['instance-id']
    ec2_resource = boto3.resource('ec2')
    instance = ec2_resource.Instance(instance_id)

    # Extract instance name from tags
    instance_name = next((tag['Value'] for tag in instance.tags if tag['Key'] == 'Name'), '')
    instance_name = instance_name.replace(' ', '-').lower() # kabeb case btw...

    # Get public IP
    instance_ip = instance.public_ip_address

    # Update Route 53
    route53_client = boto3.client('route53')
    hosted_zone_id = 'Z0000...' # get the hosted_zone_id from route53
    domain_name = f"{instance_name}.example.org"

    route53_client.change_resource_record_sets(
        HostedZoneId=hosted_zone_id,
        ChangeBatch={
            'Changes': [
                {
                    'Action': 'UPSERT',
                    'ResourceRecordSet': {
                        'Name': domain_name,
                        'Type': 'A',
                        'TTL': 300,
                        'ResourceRecords': [{'Value': instance_ip}]
                    }
                }
            ]
        }
    )
    print(f"Updated Route 53 record for {instance_name}")
