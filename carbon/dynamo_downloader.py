import boto3
import csv

# Initialize a DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Select your DynamoDB table
table = dynamodb.Table('american-chip-cloud-instances-compare')

# Initialize scan operation
response = table.scan()

# Get all unique headers
headers = set()
for item in response['Items']:
    for key in item.keys():
        headers.add(key)

# Create CSV file
with open('dynamo_download.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    for item in response['Items']:
        writer.writerow({header: item.get(header) for header in headers})
        
    # Check if there are more items to fetch
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        for item in response['Items']:
            writer.writerow({header: item.get(header) for header in headers})
