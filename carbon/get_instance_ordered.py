import boto3
from boto3.dynamodb.conditions import Attr

# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Reference the table
table = dynamodb.Table('american-chip-cloud-instances-compare')

# Query the table
response = table.scan(
    FilterExpression=Attr('graviton_suggestion').ne('no_equivalent')
)

# Parse out the instance_ids from the response items
instance_ids = [item['instance_id'] for item in response['Items']]

# Sort the instance_ids
instance_ids.sort()

# Write the output to a file
with open('instances_list.ts', 'w') as f:
    for instance_id in instance_ids:
        f.write(f'  | "{instance_id}"\n')
