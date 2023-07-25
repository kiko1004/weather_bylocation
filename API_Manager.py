import requests
import json

with open("config.json") as config:
    API_KEY = json.load(config)['token']

class API_Manager:

    @staticmethod
    def get_current_weather(q):
        url = "https://weatherapi-com.p.rapidapi.com/current.json"

        querystring = {"q":q}

        headers = {
            "X-RapidAPI-Key": API_KEY,
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring).json()
        return f'{response["location"]["name"]}, {response["current"]["temp_c"]}C'