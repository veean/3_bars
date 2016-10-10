import json
import os


def load_data(path_file):
    if not os.path.exists(filepath):
        return None
    with open(path_file, 'r', encoding="utf-8") as file_handler:
        return json.load(file_handler)


def get_biggest_bar(data):
    biggest_bar_name = ''
    biggest_bar = float('-inf')
    for bars in data:
        if bars['Cells']['SeatsCount'] >= biggest_bar:
            biggest_bar = bars['Cells']['SeatsCount']
            biggest_bar_name = bars['Cells']['Name']
    return biggest_bar_name


def get_smallest_bar(data):
    smallest_bar_name = []
    smallest_bar = float('inf')
    for bars in data:
        if bars['Cells']['SeatsCount'] <= smallest_bar:
            smallest_bar = bars['Cells']['SeatsCount']
            smallest_bar_name = bars['Cells']['Name']
    return smallest_bar_name


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
                print("Try better : %s" % (e.args[1]))
