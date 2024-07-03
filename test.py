import os
import sys
from pyupdater.client import Client

CLIENT_CONFIG = {
    'PUBLIC_KEY': 'YOUR_PUBLIC_KEY_HERE',
    'APP_NAME': 'ActiSync',
    'COMPANY_NAME': 'IntelliMotion Matrix',
    'HTTP_TIMEOUT': 30,
    'MAX_DOWNLOAD_RETRIES': 3,
    'UPDATE_URLS': ['https://raw.githubusercontent.com/jeffTW84/ActiSync_server/updates/']
}

def print_status_info(info):
    total = info.get(u'total')
    downloaded = info.get(u'downloaded')
    status = info.get(u'status')
    print(f'Downloaded {downloaded} of {total} - Status: {status}')

def check_for_updates():
    client = Client(CLIENT_CONFIG)
    app_update = client.update_check(CLIENT_CONFIG['APP_NAME'], '1.0.0')

    if app_update is not None:
        print('Update found!')
        print(f'Current version: 1.0.0')
        print(f'Latest version: {app_update.version}')

        app_update.download(print_status_info)
        if app_update.is_downloaded():
            print('Update downloaded successfully')
            app_update.extract_restart()
        else:
            print('Update download failed')
    else:
        print('No update available')

if __name__ == '__main__':
    check_for_updates()
    for i in range(10000):
        print("Check")
