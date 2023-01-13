# gets a s3 object and prints its contents
import boto3
def lambda_handler(event, context):
    s3=boto3.client('s3')

    if event:
        print('Event: ',event) # this is new change
        print('Event Type:',type(event))
        file_obj=event['Records'][0]
        filename=str(file_obj['s3']['object']['key'])
        print('filename: ',filename)
        s3obj=s3.get_object(Bucket='basic-lambda-s3',Key=filename)
        print('Bucket object :',s3obj)
        s3obj_content=s3obj['Body'].read().decode('utf-8')
        print(s3obj_content)
    return {
        'statusCode': 200,
        }
