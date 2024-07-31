import csv

class AirportModel:
    """
    Модель для работы с данными аэропортов из CSV-файла.

    Класс AirportModel загружает данные аэропортов из CSV-файла, сохраняет их в память и предоставляет методы для фильтрации данных.
    """

    def __init__(self, csv_file_path):
        """
        Инициализация модели с указанием пути к CSV-файлу.

        :param csv_file_path: Путь к файлу CSV с данными аэропортов.
        """
        self.csv_file_path = csv_file_path
        self.data = self._load_data()

    def _load_data(self):
        """
        Загрузка данных из CSV-файла в память.

        Читает CSV-файл и преобразует данные широты и долготы в float. Пропускает строки с некорректными данными.

        :return: Список словарей с информацией об аэропортах.
        """
        data = []
        with open(self.csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter='|')
            for row in reader:
                try:
                    latitude = float(row['latitude'])
                    longitude = float(row['longitude'])
                except ValueError:
                    continue

                data.append({
                    'id': row['id'],
                    'airport': row['airport'],
                    'city': row['city'],
                    'country': row['country'],
                    'iata': row['iata'],
                    'icao': row['icao'],
                    'latitude': latitude,
                    'longitude': longitude,
                    'elevation': row['elevation'],
                    'utc': row['utc'],
                    'dst': row['dst'],
                    'region': row['region']
                })
        return data

    def filter_airports(self, min_lat, max_lat, min_lon, max_lon, city_query='', country_query=''):
        """
        Фильтрация аэропортов по широте, долготе, городу и стране.

        :param min_lat: Минимальная широта.
        :param max_lat: Максимальная широта.
        :param min_lon: Минимальная долгота.
        :param max_lon: Максимальная долгота.
        :param city_query: Строка поиска по городу.
        :param country_query: Строка поиска по стране.
        :return: Список словарей с информацией об аэропортах, удовлетворяющих условиям фильтрации.
        """
        return [
            airport for airport in self.data
            if (min_lat <= airport['latitude'] <= max_lat and
                min_lon <= airport['longitude'] <= max_lon and
                (city_query.lower() in airport['city'].lower() if city_query else True) and
                (country_query.lower() in airport['country'].lower() if country_query else True))
        ]
