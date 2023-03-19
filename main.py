import json
import requests
from db import SettingsDAO


def suggest(query, resource, settingsDAO) -> dict:
    url = settingsDAO.get_url() + resource
    headers = {
        'Authorization': 'Token ' + settingsDAO.get_key(),
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    data = {
        'query': query,
        'language': settingsDAO.get_lang()
    }
    res = requests.post(url, data=json.dumps(data), headers=headers)
    return res.json()

    
def set_settings():
    key:str=input("введите свой API_KEY: ")
    lang:str = ''
    while lang != "ru" and lang != "en":
        lang=input("введите язык на котором будет работать программа 'ru' или 'en': ")
    settingsDAO.set_key(key)
    settingsDAO.set_lang(lang)





if __name__ == "__main__":
    while True:
        settingsDAO = SettingsDAO("db.db")
        print("1.использовать существующие настройки \n2.изменить настройки\n3.выход: ")
        ans:str = input("выберите действие 1, 2 или 3 и нажмите enter: ")

        if ans == '1':
            settings:list = settingsDAO.get_settings()[0]
            print("ваш API_KEY - ", settings[2])
            print("ваш язык - ", settings[3])
            
            ans:str = input("оставить эти настройки? введите 'y' или 'n': ")

            if ans == 'y':
                pass

            elif ans == 'n':
                set_settings()
                continue


        elif ans == '2':
            set_settings()
            continue

        elif ans == '3':
            break

        
        while True:
            query:str = input("введите адрес в произвольной форме или 'exit' для выхода: ")
            if(query == 'exit'):
                break

            data:dict = suggest(query, 'address', settingsDAO)

            try:
                for i in range(0, len(data['suggestions'])):
                    print(str(i+1), data['suggestions'][i]['value'])

                coordinates:int = input("\nвыберите адрес для которого нужно напечатать координаты или 'exit' для выхода: ")
                if(coordinates == 'exit'):
                    break

                print(data['suggestions'][int(coordinates)-1]['data']['geo_lat'], data['suggestions'][int(coordinates)-1]['data']['geo_lon'])

            except Exception:
                print("неверно введён API_KEY")
                break

        




