import json

def bad_request(data='bad request'):
    return {
        'statusCode': 400,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(data)
    }