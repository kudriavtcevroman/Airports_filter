from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QHBoxLayout, QMessageBox
)

class AirportView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.min_lat_label = QLabel('Min Latitude:', self)
        self.min_lat_input = QLineEdit(self)

        self.max_lat_label = QLabel('Max Latitude:', self)
        self.max_lat_input = QLineEdit(self)

        self.min_lon_label = QLabel('Min Longitude:', self)
        self.min_lon_input = QLineEdit(self)

        self.max_lon_label = QLabel('Max Longitude:', self)
        self.max_lon_input = QLineEdit(self)

        self.city_search_label = QLabel('Search by City:', self)
        self.city_search_input = QLineEdit(self)

        self.country_search_label = QLabel('Search by Country:', self)
        self.country_search_input = QLineEdit(self)

        self.filter_button = QPushButton('Apply Filter', self)

        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['City', 'Country', 'Latitude', 'Longitude'])

        self.table.setSortingEnabled(True)

        form_layout = QHBoxLayout()
        form_layout.addWidget(self.min_lat_label)
        form_layout.addWidget(self.min_lat_input)
        form_layout.addWidget(self.max_lat_label)
        form_layout.addWidget(self.max_lat_input)
        form_layout.addWidget(self.min_lon_label)
        form_layout.addWidget(self.min_lon_input)
        form_layout.addWidget(self.max_lon_label)
        form_layout.addWidget(self.max_lon_input)

        self.table.setColumnWidth(0, 161)
        self.table.setColumnWidth(1, 161)
        self.table.setColumnWidth(2, 200)
        self.table.setColumnWidth(3, 200)

        search_layout = QHBoxLayout()
        search_layout.addWidget(self.city_search_label)
        search_layout.addWidget(self.city_search_input)
        search_layout.addWidget(self.country_search_label)
        search_layout.addWidget(self.country_search_input)

        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addLayout(search_layout)
        layout.addWidget(self.filter_button)
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.setWindowTitle('Airport Filter')
        self.setGeometry(100, 100, 800, 600)

    def set_table_data(self, data):
        self.table.setRowCount(len(data))
        self.table.clearContents()
        for row, airport in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(airport['city']))
            self.table.setItem(row, 1, QTableWidgetItem(airport['country']))
            self.table.setItem(row, 2, QTableWidgetItem(str(airport['latitude'])))
            self.table.setItem(row, 3, QTableWidgetItem(str(airport['longitude'])))

    def show_error(self, message):
        error_dialog = QMessageBox(self)
        error_dialog.setIcon(QMessageBox.Icon.Critical)
        error_dialog.setWindowTitle("Error")
        error_dialog.setText(message)
        error_dialog.show()




