import time

import requests


def main():
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open('user-avatars/tshirt.jpg', 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': 'ZScUve4ZaM2NnvPt1jMGAmLm'},
    )
    if response.status_code == requests.codes.ok:
        with open('no-bg.png', 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)


API_WEATHER_TOKEN = 'your_token_here'


def get_weather():
    # http://api.weatherstack.com/current
    #     ? access_key = YOUR_ACCESS_KEY
    #     & query = New York

    response = requests.get('http://api.weatherstack.com/current',
                            params={'access_key': API_WEATHER_TOKEN,
                                    'query': 'Saint Petersburg'})

    pass


def print_emoji_based_on_weather():
    response = requests.get('http://api.weatherstack.com/current',
                     params={'access_key': 'your_api_token_here',
                             'query': 'Saint Petersburg'})

    weather_json = response.json()

    weather_type = weather_json['current']['weather_descriptions'][0]
    # weather_type = weather_json['current']  # uncomment to get valid, but incorrect behaviour

    # The simple 'database' is a text file, where you append new lines.
    with open('weather.txt', 'a') as file:
        file.write(f'{weather_type} {time.time()}\n')

    print('😀' if weather_type == 'Sunny' else '🥵')


if __name__ == '__main__':
    # main()
    # get_weather()

    print_emoji_based_on_weather()