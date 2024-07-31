class AirportController:
    """
    Контроллер для управления взаимодействием между model и view.

    Класс AirportController обрабатывает пользовательский ввод, взаимодействует с model для получения данных
    и обновляет view в соответствии с этими данными.
    """
    def __init__(self, model, view):
        """
        Инициализация контроллера с указанием model и view.

        :param model: Экземпляр класса модели.
        :param view: Экземпляр класса представления.
        """
        self.model = model
        self.view = view
        self.view.filter_button.clicked.connect(self.apply_filter)

        self.load_all_airports()

    def load_all_airports(self):
        """
        Загрузка и отображение всех данных аэропортов.

        Получает все данные из model и отображает их в view.
        """
        try:
            all_data = self.model.data
            self.view.set_table_data(all_data)
        except Exception as e:
            self.view.show_error(f"An error occurred while loading data: {str(e)}")

    def apply_filter(self):
        """
        Обработка нажатия кнопки фильтрации.

        Считывает введенные пользователем параметры фильтрации и отображает отфильтрованные данные.
        """
        try:
            min_lat = float(self.view.min_lat_input.text()) if self.view.min_lat_input.text() else -90.0
            max_lat = float(self.view.max_lat_input.text()) if self.view.max_lat_input.text() else 90.0
            min_lon = float(self.view.min_lon_input.text()) if self.view.min_lon_input.text() else -180.0
            max_lon = float(self.view.max_lon_input.text()) if self.view.max_lon_input.text() else 180.0
        except ValueError:
            self.view.show_error("Invalid input! Please enter valid numbers for latitude and longitude.")
            return

        city_query = self.view.city_search_input.text().strip().lower()
        country_query = self.view.country_search_input.text().strip().lower()

        try:
            filtered_data = self.model.filter_airports(
                min_lat, max_lat, min_lon, max_lon, city_query, country_query
            )
            self.view.set_table_data(filtered_data)
        except Exception as e:
            self.view.show_error(f"An error occurred during filtering: {str(e)}")

