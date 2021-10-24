import datetime
from Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
DESCRIPTION_TEMPLATE = '''
Upload Date: {}

This video is uploaded by YoutubeAutoUploader
Created by deXOR0

Check out YoutubeAutoUploader on GitHub!
--GitHub Link--

Follow deXOR0 on GitHub!
https://github.com/deXOR0
'''

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

def upload(video_file_path, video_title):
    upload_date_time = datetime.datetime.now()

    request_body = {
        'snippet': {
            'categoryId': 28,
            'title': video_title,
            'description': DESCRIPTION_TEMPLATE.format(str(upload_date_time)),
            'tags': ['YoutubeAutoUploader']
        },
        'status': {
            'privacyStatus': 'private',
            'selfDeclaredMadeForKids': False, 
        },
        'notifySubscribers': False
    }

    print(request_body)

    mediaFile = MediaFileUpload(video_file_path)

    response_upload = service.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=mediaFile
    ).execute()

    return response_upload.get('id')