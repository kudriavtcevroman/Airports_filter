import csv

class AirportModel:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.data = self._load_data()

    def _load_data(self):
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
        return [
            airport for airport in self.data
            if (min_lat <= airport['latitude'] <= max_lat and
                min_lon <= airport['longitude'] <= max_lon and
                (city_query.lower() in airport['city'].lower() if city_query else True) and
                (country_query.lower() in airport['country'].lower() if country_query else True))
        ]
