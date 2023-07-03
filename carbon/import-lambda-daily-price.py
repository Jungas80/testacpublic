import boto3
import csv
import io
from botocore.exceptions import ClientError
from decimal import Decimal

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # Get the bucket and object key from the Event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Get the object from the event and show its content type
    csv_file = s3_client.get_object(Bucket=bucket, Key=key)
    csv_content = csv_file['Body'].read().decode('utf-8')

    # Open the file and read the content
    data = io.StringIO(csv_content)
    next(data)  # Skip the header
    for row in csv.reader(data):
        instance_id = row[0]
        daily_price = Decimal(row[1])  # convert to Decimal

        # Get the table resource
        table = dynamodb.Table('american-chip-cloud-instances-compare')

        # Update the table
        try:
            response = table.update_item(
                Key={
                    'cloud_provider_id': 'aws',
                    'instance_id': instance_id
                },
                UpdateExpression="set daily_price = :p",
                ExpressionAttributeValues={
                    ':p': daily_price
                },
                ReturnValues="UPDATED_NEW"
            )

        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("UpdateItem succeeded:")
            print(response)

    return 'Processing completed'
