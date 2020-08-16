import json
import boto3

def lambda_handler(event, context):
    #gives details of sqs message
    #message can be fetched from body and messageAttributes(metadata)
    #print(event)

    #and perform any processing with sqs event data
    # below example writes    
    s3 = boto3.client('s3')
    data = json.loads(event['Records'][0]['body'])
    s3.put_object(Bucket="sqs-demo-tut", Key="data.json", Body=json.dumps(data))
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
