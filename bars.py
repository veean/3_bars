import json
import os
import argparse


def load_data(path_file):
    if not os.path.exists(path_file):
        return None
    with open(path_file, 'r', encoding="utf-8") as file_handler:
        return json.load(file_handler)


def get_biggest_bar(data):
    bar = max(data, key=lambda x: x['Cells']['SeatsCount'])
    return bar['Cells']['Name']


def get_smallest_bar(data):
    bar = min(data, key=lambda x: x['Cells']['SeatsCount'])
    return bar['Cells']['Name']


def count_distance(data_unit, longitude, latitude):
    distance = (longitude - data_unit['Cells']['geoData']['coordinates'][0]) ** 2 + (latitude - data_unit['Cells'][
        'geoData']['coordinates'][1]) ** 2
    return distance


def get_closest_bar_subver(data, longtitude, latitude):

    bar = min(data, key=lambda x: count_distance(x, float(longtitude), float(latitude)))
    return bar['Cells']['Name']


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Analysin lots of Moscow bars")
    parser.add_argument('-file', help='Путь к json файлу')
    parser.add_argument('-ln', help="Ваши координаты : текущая широта")
    parser.add_argument('-lt', help="Ваши координаты : текущая долгота")
    args = parser.parse_args()

    filepath = str(args.file).encode('ascii').decode('utf-8')

    if not args.file:
        print('Try again with arguments!')
    else:
        try:
            pretty_data = load_data(filepath)
            print('Зе biggest бар: ', get_biggest_bar(pretty_data))
            print('Зе smallest бар: ', get_smallest_bar(pretty_data))
            if args.ln and args.lt:
                print('Ближайший бар:', get_closest_bar_subver(pretty_data, args.ln, args.lt))

        except FileNotFoundError as e:
            print("Try better : {}".format(e.args[1]))
