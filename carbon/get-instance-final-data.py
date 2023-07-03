import json
import boto3
import csv
from io import StringIO
from decimal import Decimal
import logging

dynamodb = boto3.resource('dynamodb')
s3_client = boto3.client('s3')
table = dynamodb.Table('american-chip-cloud-instances-compare')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    csv_file = event['Records'][0]['s3']['object']['key']
    response = s3_client.get_object(Bucket=bucket, Key=csv_file)
    data = response["Body"].read().decode('utf-8')
    data = csv.reader(StringIO(data))
    next(data)  # skip the header
    results = []
    for row in data:
        instance_id = row[0]
        response = table.get_item(Key={'cloud_provider_id': 'aws', 'instance_id': instance_id})
        if 'Item' in response:
            item = response['Item']
            daily_price = item.get('daily_price')
            gCO2eq24hs = item.get('gCO2eq24hs')
            result = {
                'instance_id': instance_id,
                'daily_price': daily_price,
                'gCO2eq24hs': gCO2eq24hs,
                'graviton_suggestion': item.get('graviton_suggestion')
            }
            if item.get('graviton_suggestion'):
                graviton_response = table.get_item(Key={'cloud_provider_id': 'aws', 'instance_id': item.get('graviton_suggestion')})
                if 'Item' in graviton_response:
                    graviton_item = graviton_response['Item']
                    graviton_daily_price = graviton_item.get('daily_price')
                    graviton_gCO2eq24hs = graviton_item.get('gCO2eq24hs')
                    result['graviton_daily_price'] = graviton_daily_price
                    result['graviton_gCO2eq24hs'] = graviton_gCO2eq24hs
                    if daily_price != 0:
                        cost_reduction = ((daily_price - graviton_daily_price) / daily_price) * 100
                        result['cost_reduction'] = "{:.2f}%".format(cost_reduction)
                    if gCO2eq24hs != 0:
                        carbon_footprint_reduction = ((gCO2eq24hs - graviton_gCO2eq24hs) / gCO2eq24hs) * 100
                        result['carbon_footprint_reduction'] = "{:.2f}%".format(carbon_footprint_reduction)
            results.append(result)

    json_results = json.dumps(results, cls=DecimalEncoder)
    logger.info('Results: %s', json_results)

    return {
        'statusCode': 200,
        'body': json_results
    }
