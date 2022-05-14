import requests


class YaUploader:
    upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    @property
    def header(self):
        return self.get_headers()

    def _get_upload_link(self, file_name: str):
        params = {'path': file_name, 'overwrite': 'true'}
        response = requests.get(self.upload_url, params=params, headers=self.header)
        return response.json()

    def upload(self, file_path: str, file_name: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        href = self._get_upload_link(file_name).get('href')
        if not href:
            return False

        response = requests.put(href, data=open(f'{file_path}\\{file_name}', 'rb'))
        if response.status_code == 201:
            print('Файл загружен')
            return True


path_to_file = input('Введите путь к загружаемому файлу: ')
file_name = input('Введите имя загружаемого файла: ')
token = input('Введите ваш токен: ')
uploader = YaUploader(token)
result = uploader.upload(path_to_file, file_name)
