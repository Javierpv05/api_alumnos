import boto3

def lambda_handler(event, context):
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    response = table.get_item(
        Key={'tenant_id': tenant_id, 'alumno_id': alumno_id}
    )
    item = response.get('Item', {})
    return {'statusCode': 200, 'alumno': item}
