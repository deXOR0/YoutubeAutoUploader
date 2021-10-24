import os
from colorama import init as colorama_init
from termcolor import colored
from uploader import upload

VIDEO_SOURCE = 'video'
SUPPORTED_VIDEO_FORMAT = ('mp4', 'mkv', 'mov')

def error(msg):
    print(colored(f'[Error] {msg}\n', 'red'))

def warning(msg):
    print(colored(f'[Warning] {msg}\n', 'yellow'))

def success(msg):
    print(colored(f'[Success] {msg}\n', 'green'))

def init():
    print('''
█▄█ █▀█ █░█ ▀█▀ █░█ █▄▄ █▀▀   ▄▀█ █░█ ▀█▀ █▀█   █░█ █▀█ █░░ █▀█ ▄▀█ █▀▄ █▀▀ █▀█
░█░ █▄█ █▄█ ░█░ █▄█ █▄█ ██▄   █▀█ █▄█ ░█░ █▄█   █▄█ █▀▀ █▄▄ █▄█ █▀█ █▄▀ ██▄ █▀▄
                             Created by deXOR0
    ''')

    if not os.path.exists(VIDEO_SOURCE):
        error('Video Source Directory not found!')
        warning('Creating Video Source Directory...')
        os.mkdir(VIDEO_SOURCE)
        success('Created Video Source Directory')
    else:
        success('Video Source Directory Found!')

def queue_videos():
    warning(f'Looking for video files on {VIDEO_SOURCE}...')
    videos = os.listdir(VIDEO_SOURCE)

    if not videos:
        error('No video files are found!')
        warning(f'Make sure video files are of {", ".join(SUPPORTED_VIDEO_FORMAT)} format')
    else:
        success(f'Found {len(videos)} video files!')
        print('Video Queue')
        for i in range(len(videos)):
            print(f'{i+1}. {videos[i]}')
    
    return videos

if __name__ == '__main__':
    colorama_init()
    init()
    video_queue = queue_videos()
    for v in video_queue:
        warning(f'Uploading {v}...')
        video_file = os.path.join(VIDEO_SOURCE, v)
        video_id = upload(video_file, v)
        success(f'{v} has been successfully uploaded! You can watch it on https://www.youtube.com/watch?v={video_id}')
        warning(f'Deleting {video_file} from Video Source Folder...')
        os.delete(video_file)
        success(f'Deleted {video_file}')