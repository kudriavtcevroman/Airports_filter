import sys
from PyQt6.QtWidgets import QApplication
from model import AirportModel
from view import AirportView
from controller import AirportController

if __name__ == '__main__':
    app = QApplication(sys.argv)

    model = AirportModel('airports.csv')
    view = AirportView()
    controller = AirportController(model, view)

    view.show()
    sys.exit(app.exec())
