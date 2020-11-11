import requests, os, keyboard, json
from time import sleep
from git.repo.base import Repo

class RepositoryManipulation:
    __user = 'EnergyWork'
    __token = ''
    __headers = { 
        'Authorization' : f'token {__token}',
        'Accept': 'application/vnd.github.v3+json' 
    }
    __repos_url = 'https://api.github.com/user/repos'
    __del_repos_url = f'https://api.github.com/repos' # + user + repos_name
    def __init__(self):
        pass
    @property
    def headers(self):
        return self.__headers
    @property
    def repos_url(self):
        return self.__repos_url
    @property
    def del_repos_url(self):
        return self.__del_repos_url
    @property
    def user(self):
        return self.__user

class CreateRepository(RepositoryManipulation):
    data = {
        'name': 'delete-this-repos',
        'description': 'description',
        'homepage': 'https://github.com',
        'private': False,
        'auto_init' : True
    }
    def __init__(self, name='', description=''):
        super().__init__()
        if name and not name.isspace():
            self.data['name'] = name
        if not (description and not description.isspace()):
            self.data['auto_init'] = False
        else:
            self.data['description'] = description
    def create(self):
        response = requests.post(self.repos_url, data=json.dumps(self.data), headers=self.headers)
        return response
    def clone(self):
        pass

class DeleteRepository(RepositoryManipulation):
    def __init__(self):
        super().__init__()  
    def delete(self, name):
        url = f'{self.del_repos_url}/{self.user}/{name}'
        response = response = requests.delete(url=url, headers=self.headers)
        return response

class ConsoleApplication:
    ## CONSTRUCTOR ##############################################################################
    def __init__(self):
        pass
    #############################################################################################
    def __YN(self):
        while True:
            if keyboard.is_pressed('y'):
                return True
            elif keyboard.is_pressed('n'):
                return False
    #############################################################################################
    def __stop(self):
        print('Нажмите пробел, чтобы закрыть окно')
        keyboard.wait('space')
    #############################################################################################
    def __create_repos(self):
        name_repo = input('Название репозитория: ')
        description = input('Описание: ')
        result = CreateRepository(name=name_repo, description=description).create()
        if result.status_code == 201:
            resp = result.json()
            print('Успешно создан репозиторий:', resp['name'])
            print('Ссылка:', resp['html_url'])
            print('Клонировать? Y/N')
            res = self.__YN()
            if res:
                print('Клонирование')
                os.system('git clone {}'.format(resp['html_url']))
            else:
                print('Отмена клонирования')
            # Repo.clone_from(resp['html_url'], resp['name'])
        else:
            print('Ошибка при создании, код:', result.status_code)
    #############################################################################################
    def __craete_and_clone(self):
        path = os.path.split(os.path.abspath(__file__))[0]
        print(f'Создание удаленного репозитория и клонирование его в {path}')
        print('Продолжить? Y/N')
        while True:
            if keyboard.is_pressed('n'):
                break
            elif keyboard.is_pressed('y'):
                self.__create_repos()
                break
    ############################################################################################# 
    def __delete_repos(self):
        name = input('Введите название репозитория: ')
        result = DeleteRepository().delete(name)
        if result.status_code == 204:
            print('Статус:', result.status_code, 'репозиторий успешно удалён')
        else:
            print('Ошибка при удалении', result.status_code)
    ############################################################################################# 
    def start_application(self):
        print('---github.com/EnergyWork---')
        print('Создание/удаление/выход? C/D/Esc')
        while True:
            if keyboard.is_pressed('c'):
                self.__craete_and_clone()
                self.__stop()
                break
            elif keyboard.is_pressed('d'):
                self.__delete_repos()
                self.__stop()
                break
            elif keyboard.is_pressed('esc'):
                break

if __name__ == "__main__":
    app = ConsoleApplication()
    app.start_application()
