# 3_bars
Скрипт показывает самый большой и маленький бар в г.Москва, 
а так же по введенным координатам определяет самый близкий бар. 
Для этого необходимо скачать файл в формате json по ссылке:

*http://data.mos.ru/opendata/export/1796/json/2/1

Запускается скрипт с указанием в качестве первого параметра название
и путь до файла в кавычках с указанием расширения.
Пример: python bars.py 'filename.json'

В случае не правильного ввода названия файла или в случае его отсутствии программа предлагает ввести путь заново.
