import json

def internal_server_error(data='internal server error'):
    return {
        'statusCode': 500,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(data)
    }