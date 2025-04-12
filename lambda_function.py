import boto3
import os
from PIL import Image
import io
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

SOURCE_BUCKET = os.getenv('SOURCE_BUCKET')
PROCESSED_BUCKET = os.getenv('PROCESSED_BUCKET')
DYNAMODB_TABLE = os.getenv('DYNAMODB_TABLE')

def lambda_handler(event, context):
    try:
        record = event['Records'][0]
        bucket_name = event['Records']['s3']['bucket']['name']
        object_key = event['Records']['s3']['object']['key']

        print(f"Processing file: {object_key} from bucket: {bucket_name}")

        response = s3.get_object(Bucket=bucket_name, key=object_key)
        image_data = response['Body'].read()

        image = Image.open(io.BytesIO(image_data))

        resized_image = image.resize((300,300))

        buffer =  io.BytesIO()
        resized_image.save(buffer, format=image.format)
        buffer.seek(0)

        processed_key = f"processed/{object_key}"
        s3.put_object(Bucket=PROCESSED_BUCKET, key=processed_key, Body=buffer)

        print(f"Processed image saved to: {PROCESSED_BUCKET}/{processed_key}")

        table = dynamodb.Table(DYNAMODB_TABLE)
        table.put_item(item={
            'ImageID' : object_key,
            'ProcessedURL' : f"s3://{PROCESSED_BUCKET}/{processed_key}",
            'Size': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        
        print(f"MetaData saved to DynamoDB table: {DYNAMODB_TABLE}")

        return{
            'status code' : 200,
            'body' : f"Successfully processed file: {object_key}"
        }

    except Exception as e:
        print(f"Error processing file: {e}")
        return {
            'statusCode': 500,
            'body': f"Error processing file: {e}"
        }