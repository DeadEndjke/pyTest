import json
import requests
from db import UserDAO
from user import User


def suggest(query, resource, userDAO, id):
    url = userDAO.get_url(id) + resource
    headers = {
        'Authorization': 'Token ' + userDAO.get_key(id),
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    data = {
        'query': query,
        'language': userDAO.get_lang(id)
    }
    res = requests.post(url, data=json.dumps(data), headers=headers)
    return res.json()






if __name__ == "__main__":
    while True:
        userDAO = UserDAO("db.db")
        print("1.выбрать уже существующий аккаунт")
        print("2.создать новый аккаунт")
        print("3.выход")
        ans = input("выберите действие 1, 2 или 3 и нажмите enter ")
        if ans == '1':
            userDAO.showAll()
            selected = input("выберите аккаунт или напишите 'exit' для выхода ")
            if selected == 'exit':
                break
        elif ans == '2':
            key=input("введите свой API_KEY ")
            lang=input("введите язык на котором будет работать программа 'ru' или 'en' ")
            user = User(key, lang)
            userDAO.add_user(user)
            selected = userDAO.get_max_id()
        elif ans == '3':
            break

        
        while True:
            query:str = input("введите адрес в произвольной форме или 'exit' для выхода: ")
            if(query == 'exit'):
                break

            data = suggest(query, 'address', userDAO, str(selected))

        
            for i in range(0, len(data['suggestions'])):
                print(str(i+1), data['suggestions'][i]['value'])

            print()

            coordinates:int = input("выберите адрес для которого нужно напечатать координаты или 'exit' для выхода: ")
            if(coordinates == 'exit'):
                break

            print(data['suggestions'][int(coordinates)-1]['data']['geo_lat'], data['suggestions'][int(coordinates)-1]['data']['geo_lon'])

        




