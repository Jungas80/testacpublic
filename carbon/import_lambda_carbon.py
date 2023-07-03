import boto3
import csv
import io
from botocore.exceptions import ClientError

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
        gCO2eq24hs = float(row[1])  # get the value

        # Get the table resource
        table = dynamodb.Table('american-chip-cloud-instances-compare')

        # Update the table
        try:
            response = table.update_item(
                Key={'instance_id': instance_id},
                UpdateExpression="set gCO2eq24hs = :g",
                ExpressionAttributeValues={
                    ':g': gCO2eq24hs
                },
                ReturnValues="UPDATED_NEW"
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("UpdateItem succeeded:")
            print(response)

    return 'Processing completed'
