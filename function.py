import boto3
import json

def get_data():
   
    s3_bucket = 'buckect_name'
    
    data = []
    
    s3 = boto3.client('s3')
    objects = s3.list_objects_v2(Bucket = s3_bucket)['Contents']
    
    print('objects: ',objects)
    
    s3_keys = []
    
    for obj in objects:
        if obj['Key'].startswith('users_'):
            s3_keys.append(obj['Key'])
            
    print('s3_keys: ',s3_keys)
   
    for key in s3_keys:
        obj = s3.get_object(Bucket=s3_bucket,Key = key)
        obj_data = json.loads(obj['Body'].read())
        data.append(obj_data)
        
    return data

def handler(event, context):
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'body': json.dumps(get_data()), 
        'headers': {"Access-Control-Allow-Origin": "*"}}
