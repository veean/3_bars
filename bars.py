import json
import os


def load_data(path_file):
    if not os.path.exists(filepath):
        return None
    with open(path_file, 'r', encoding="utf-8") as file_handler:
        return json.load(file_handler)


def get_biggest_bar(data):
    bar = max(data, key=lambda x: x['Cells']['SeatsCount'])
    return bar['Cells']['Name']



def get_smallest_bar(data):
    bar = min(data, key=lambda x: x['Cells']['SeatsCount'])
    return bar['Cells']['Name']



def get_closest_bar(data, longitude, latitude):
    min_distance = float('inf')
    name_bar = ''
    for name in data:
        distance = (longitude - name['Cells']['geoData']['coordinates'][0]) ** 2 + (latitude - name['Cells']['geoData'][
            'coordinates'][1]) ** 2
        if distance < min_distance:
            min_distance = distance
            name_bar = name['Cells']['Name']

    return name_bar


if __name__ == '__main__':
    while True:
        filepath = input('Введите путь до json файла: ')

        print('Введите координаты своего местоположения')

        user_longitude = float(input('Долгота :'))
        user_latitude = float(input('Широта:'))

        if not filepath and user_longitude and user_latitude:
            print('Try again!')
        else:
            try:
                pretty_data = load_data(filepath)
                print('Ближайший бар:', get_closest_bar(pretty_data, user_longitude, user_latitude))

                print('Зе biggest бар: ', get_biggest_bar(pretty_data))
                print('Зе smallest бар: ', get_smallest_bar(pretty_data))
                break
            except IOError as e:
                print("Try better : {}".format(e.args[1]))
