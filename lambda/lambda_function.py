import boto3
import json
import uuid

translate = boto3.client('translate', region_name='eu-west-1')
polly = boto3.client('polly', region_name='eu-west-1')
s3 = boto3.client('s3', region_name='eu-west-1')

BUCKET_NAME = 'translate-polly-giles-2025'

def lambda_handler(event, context):
    try:
        print("Event Received:", json.dumps(event))
        body = json.loads(event['body'])
        text = body['text']
        language = body['language']

        # Translate text
        translated = translate.translate_text(
            Text=text,
            SourceLanguageCode='en',
            TargetLanguageCode=language
        )
        translated_text = translated['TranslatedText']

        # Synthesize speech
        audio = polly.synthesize_speech(
            Text=translated_text,
            OutputFormat='mp3',
            VoiceId='Lucia' if language == 'es' else 'Joanna'  # Adjust voice
        )

        # Save to S3
        file_name = f"{str(uuid.uuid4())}.mp3"
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=audio['AudioStream'].read(),
            ContentType='audio/mpeg'
        )

        audio_url = f"https://{BUCKET_NAME}.s3.eu-west-1.amazonaws.com/{file_name}"

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*'
            },
            'body': json.dumps({
                'translated_text': translated_text,
                'audio_url': audio_url
            })
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
