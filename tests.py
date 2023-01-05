import unittest
from main import Tester, ACCESS_TOKEN, FILE_TO_UPLOAD

tester = Tester(ACCESS_TOKEN, FILE_TO_UPLOAD, f'{FILE_TO_UPLOAD}')

def test_file_upload():
    assert tester.file_upload().ok

def test_file_getmetadata():
    response = tester.file_getmetadata()
    assert response.json()['name'] == FILE_TO_UPLOAD
    assert response.ok

def test_file_delete():
    assert tester.file_delete().ok

if __name__ == '__main__':
    unittest.main()

