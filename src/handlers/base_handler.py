import json

def handler(event, context):
    """
    Handler base para AWS Lambda
    """
    try:
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'message': 'Lambda handler funcionando!'
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Erro interno',
                'error': str(e)
            })
        }
