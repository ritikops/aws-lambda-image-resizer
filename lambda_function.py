import boto3
from PIL import Image
import io
import json

# Initialize AWS clients
s3 = boto3.client('s3')
sns = boto3.client('sns')

# Set bucket names
SOURCE_BUCKET = "source-images-bucket"
DEST_BUCKET = "resized-images-bucket"

# Set SNS Topic ARN
SNS_TOPIC_ARN = "arn:aws:sns:ap-south-1:123456789012:ImageResizeNotification"

# Resize dimensions
RESIZE_WIDTH = 300
RESIZE_HEIGHT = 300

def lambda_handler(event, context):
    try:
        for record in event['Records']:
            source_bucket = record['s3']['bucket']['name']
            image_key = record['s3']['object']['key']
            
            # Download the image from S3
            response = s3.get_object(Bucket=source_bucket, Key=image_key)
            image_data = response['Body'].read()
            
            # Open and resize image
            image = Image.open(io.BytesIO(image_data))
            image = image.resize((RESIZE_WIDTH, RESIZE_HEIGHT))  # Resize
            
            # Convert resized image to bytes
            buffer = io.BytesIO()
            image.save(buffer, "JPEG")
            buffer.seek(0)
            
            # Upload resized image to destination bucket
            new_key = f"resized-{image_key}"
            s3.put_object(Bucket=DEST_BUCKET, Key=new_key, Body=buffer, ContentType="image/jpeg")
            
            # SNS Notification
            message = {
                "OriginalImage": f"s3://{source_bucket}/{image_key}",
                "ResizedImage": f"s3://{DEST_BUCKET}/{new_key}",
                "Message": "Image has been successfully resized and saved."
            }
            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Message=json.dumps(message),
                Subject="Image Resizing Completed"
            )
            
            print(f"Resized image uploaded to {DEST_BUCKET}/{new_key}")
        
        return {"statusCode": 200, "body": "Image resized successfully!"}
    
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        return {"statusCode": 500, "body": "Error processing image"}
