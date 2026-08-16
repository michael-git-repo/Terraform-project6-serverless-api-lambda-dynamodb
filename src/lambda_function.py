import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = os.environ.get('TABLE_NAME')
table = dynamodb.Table(TABLE_NAME)

HEADERS = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS'
}

def lambda_handler(event, context):
    http_method = event.get('requestContext', {}).get('http', {}).get('method')

    try:
        if http_method == 'POST':
            body = json.loads(event.get('body', '{}'))
            item = {
                'student_id': str(body['studentId']),
                'name': body['name'],
                'class': body['class'],
                'age': str(body['age']),
                'country': body.get('country', ''),
                'state': body.get('state', '')
            }
            table.put_item(Item=item)
            return {
                'statusCode': 200,
                'headers': HEADERS,
                'body': json.dumps({'message': 'Student Data Saved!'})
            }

        elif http_method == 'GET':
            response = table.scan()
            items = response.get('Items', [])
            return {
                'statusCode': 200,
                'headers': HEADERS,
                'body': json.dumps(items)
            }

        return {
            'statusCode': 400,
            'headers': HEADERS,
            'body': json.dumps({'error': 'Unsupported HTTP Method'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': HEADERS,
            'body': json.dumps({'error': str(e)})
        }