import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')

# Read table name from the Terraform environment variable
TABLE_NAME = os.environ.get('TABLE_NAME', 'StudentData')
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "*",
        "Access-Control-Allow-Methods": "GET, POST, OPTIONS"
    }

    http_method = event.get('requestContext', {}).get('http', {}).get('method')

    # Handle CORS Preflight
    if http_method == 'OPTIONS':
        return {'statusCode': 200, 'headers': headers, 'body': ''}

    # Handle POST (Save Student)
    if http_method == 'POST':
        try:
            body = json.loads(event.get('body', '{}'))
            
            item = {
                'student_id': str(body.get('studentId')),
                'name': body.get('name'),
                'class': body.get('class'),
                'age': str(body.get('age')),
                'country': body.get('country'),
                'state': body.get('state')
            }

            table.put_item(Item=item)

            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps({'message': 'Data saved successfully!'})
            }
        except Exception as e:
            print("Error writing to DynamoDB:", str(e))
            return {
                'statusCode': 500,
                'headers': headers,
                'body': json.dumps({'error': str(e)})
            }

    # Handle GET (View All Students)
    elif http_method == 'GET':
        try:
            response = table.scan()
            items = response.get('Items', [])
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps(items)
            }
        except Exception as e:
            print("Error scanning DynamoDB:", str(e))
            return {
                'statusCode': 500,
                'headers': headers,
                'body': json.dumps({'error': str(e)})
            }

    return {
        'statusCode': 400,
        'headers': headers,
        'body': json.dumps({'message': 'Unsupported method'})
    }