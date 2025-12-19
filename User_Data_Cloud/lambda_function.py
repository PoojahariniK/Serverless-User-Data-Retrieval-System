import json
import boto3
from botocore.exceptions import ClientError

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UserData')

def lambda_handler(event, context):
    # Extract user_id from query parameters (?id=101)
    query_params = event.get('queryStringParameters')
    user_id = query_params.get('id') if query_params else None
    
    if not user_id:
        return {
            'statusCode': 400,
            'headers': get_headers(),
            'body': json.dumps({'message': 'Missing user_id in request'})
        }

    try:
        # Fetch user profile using the partition key 'user_id'
        response = table.get_item(Key={'user_id': user_id})
        
        if 'Item' in response:
            return {
                'statusCode': 200,
                'headers': get_headers(),
                'body': json.dumps(response['Item'])
            }
        else:
            return {
                'statusCode': 404,
                'headers': get_headers(),
                'body': json.dumps({'message': 'User profile not found'})
            }
            
    except ClientError as e:
        return {
            'statusCode': 500,
            'headers': get_headers(),
            'body': json.dumps({'message': 'Server error: ' + str(e)})
        }

def get_headers():
    return {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*", # Allows your website to talk to Lambda
        "Access-Control-Allow-Methods": "GET,OPTIONS"
    }