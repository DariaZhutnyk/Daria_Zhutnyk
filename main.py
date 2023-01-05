from requests import post
from json import dumps

ACCESS_TOKEN = 'sl.BWVmQxd87mBtA-5zDXFmiQbrl9hpHIFUEy2WoMD1I6sPX-BspZRtDWy8i9_swjH03ZujRXTq5EhREUn_xHiyA2h9m421wQ_jNJOXd-WLjeGhdeoG5rbuhLUceIE8SPkODKjmEjlwpt8p'
FILE_TO_UPLOAD = 'picture.png'
RELATIVE_PATH_TO_FILE = f'{FILE_TO_UPLOAD}'

class Tester:

    def __init__(self, access_token, file_to_upload, relative_path_to_file):
        self.access_token = access_token
        self.file_to_upload = file_to_upload
        self.relative_path_to_file = relative_path_to_file

    def file_upload(self):
        url = 'https://content.dropboxapi.com/2/files/upload'
        headers = {'Authorization': f'Bearer {self.access_token}',
                   'Dropbox-API-Arg': dumps({'mode': 'add',
                                                  'autorename': True,
                                                  'mute': False,
                                                  'strict_conflict': False,
                                                  'path': f'/{self.file_to_upload}'}),
                   'Content-Type': 'application/octet-stream'}
        with open(self.relative_path_to_file, 'rb') as file:
            data_file = file.read()
            return post(url=url, headers=headers, data=data_file)

    def file_getmetadata(self):
        url = 'https://api.dropboxapi.com/2/files/alpha/get_metadata'
        headers = {'Authorization': f'Bearer {self.access_token}',
                   'Content-Type': 'application/json'}
        data = dumps({'path': f'/{self.file_to_upload}'})
        return post(url=url, headers=headers, data=data)

    def file_delete(self):
        url = 'https://api.dropboxapi.com/2/files/delete'
        headers = {'Authorization': f'Bearer {self.access_token}',
                   'Content-Type': 'application/json'}
        data = dumps({'path': f'/{self.file_to_upload}'})
        return post(url, headers=headers, data=data)


if __name__ == '__main__':
    tester = Tester(ACCESS_TOKEN, FILE_TO_UPLOAD, f'{FILE_TO_UPLOAD}')
    print(tester.file_upload())
    print(tester.file_getmetadata())
    print(tester.file_delete())



