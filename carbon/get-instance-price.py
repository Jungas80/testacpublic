import boto3
import json

def lambda_handler(event, context):
    instance_types = [event['instance_type']]
    prices = get_instance_pricing(instance_types)

    if prices:
        min_price = min(prices)  # This is the minimum hourly price
        daily_min_price = min_price * 24  # This is the minimum daily price
        daily_min_price = format(daily_min_price, '.2f')  # Format to 2 decimal places
        return {
            'statusCode': 200,
            'body': daily_min_price
        }
    else:
        return {
            'statusCode': 404,
            'body': 'No instance found with that configuration.'
        }

def get_instance_pricing(instance_types):
    pricing_client = boto3.client('pricing', region_name='us-east-1')

    response = pricing_client.get_products(
        ServiceCode='AmazonEC2',
        Filters=[
            {
                'Type': 'TERM_MATCH',
                'Field': 'instanceType',
                'Value': ','.join(instance_types)  # Join the instance types into a comma-separated string
            },
            {
                'Type': 'TERM_MATCH',
                'Field': 'termType',
                'Value': 'OnDemand'
            },
            {
                'Type': 'TERM_MATCH',
                'Field': 'location',
                'Value': 'US East (N. Virginia)'
            },
            {
                'Type': 'TERM_MATCH',
                'Field': 'operatingSystem',
                'Value': 'Linux'
            },
            {
                'Type': 'TERM_MATCH',
                'Field': 'preInstalledSw',
                'Value': 'NA'
            }
        ],
        FormatVersion='aws_v1'
    )

    price_list = response['PriceList']

    prices = []
    for price_item in price_list:
        price_item_data = json.loads(price_item)
        terms = price_item_data['terms']
        on_demand_terms = terms['OnDemand']
        for term_key in on_demand_terms:
            term_data = on_demand_terms[term_key]
            price_dimensions = term_data.get('priceDimensions', {})
            for dimension_key in price_dimensions:
                price_per_unit = price_dimensions[dimension_key]['pricePerUnit']['USD']
                if float(price_per_unit) > 0:
                    prices.append(float(price_per_unit))

    return prices
