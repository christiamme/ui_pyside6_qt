##############################################################################
##
## A desktop interface that reads information from a simulated temperature
## and humidity sensor and displays alarms. Built to try Qt with Python.
##
##############################################################################

# Import Qt libraries
from PySide6.QtWidgets import *
from PySide6.QtCore import QFile
# Import UI developed in Qt Creator
from ui_mainwindow import Ui_MainWindow
# Import PseudoSensor
from psuedoSensor import PseudoSensor
# Import system tools and datetime
import sys
import statistics
import time
from datetime import datetime

# Start the PseudoSensor
ps = PseudoSensor()
# Store the values
sensor_measurements = []
# Alarm values
temperature_alarm = 80
humidity_alarm = 75

# Create and start the Qt application
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Button to close and exit
        self.button = self.findChild(QPushButton, 'closegui')
        self.button.clicked.connect(self.closeAndExit)

        # Button to get current sensor data
        self.button = self.findChild(QPushButton, 'current_sensor')
        self.button.clicked.connect(self.showCurrent)

        # Button to get next 10 pieces of information
        self.button = self.findChild(QPushButton, 'next_10')
        self.button.clicked.connect(self.showTenValues)

        # Button to calculate statistics
        self.button = self.findChild(QPushButton, 'calculate')
        self.button.clicked.connect(self.calculateStatistics)

        # Button to set alarms
        self.button = self.findChild(QPushButton, 'set_alarm')
        self.button.clicked.connect(self.setAlarms)

        # Table with values
        self.values = self.findChild(QTableWidget, 'values')

        # Text input with temperature
        self.temp_warning = self.findChild(QTextEdit, 'temp_warning')
        # Set default value
        self.temp_warning.setPlainText(str(temperature_alarm))

        # Text input with humidity
        self.humidity_warning = self.findChild(QTextEdit, 'humidity_warning')
        # Set default value
        self.humidity_warning.setPlainText(str(humidity_alarm))

    def showCurrent(self):
        # Sensor values
        h,t = ps.generate_values()
        # Timestamp in format dd/mm/YY H:M:S
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        sensor_measurements.append([dt_string, t, h])

        # Print values in the table
        self.values.insertRow(self.values.rowCount())
        self.values.setItem(self.values.rowCount()-1, 0, QTableWidgetItem(sensor_measurements[-1][0]))
        self.values.setItem(self.values.rowCount()-1, 1, QTableWidgetItem(str(round(sensor_measurements[-1][1],4))))
        self.values.setItem(self.values.rowCount()-1, 2, QTableWidgetItem(str(round(sensor_measurements[-1][2],4))))

        # Alert if value exceeded the alarm threshold
        if sensor_measurements[-1][1] > temperature_alarm:
            QMessageBox.warning(self,'Limit Exceeded','Temperature limit exceeded.')
        if sensor_measurements[-1][2] > humidity_alarm:
            QMessageBox.warning(self,'Limit Exceeded','Humidity limit exceeded.')

    def showTenValues(self):
        for i in range(10):
            # Sensor values
            h,t = ps.generate_values()
            # Timestamp in format dd/mm/YY H:M:S
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            sensor_measurements.append([dt_string, t, h])

            # Print values in the table
            self.values.insertRow(self.values.rowCount())
            self.values.setItem(self.values.rowCount()-1, 0, QTableWidgetItem(sensor_measurements[-1][0]))
            self.values.setItem(self.values.rowCount()-1, 1, QTableWidgetItem(str(round(sensor_measurements[-1][1],4))))
            self.values.setItem(self.values.rowCount()-1, 2, QTableWidgetItem(str(round(sensor_measurements[-1][2],4))))

            # Alert if value exceeded the alarm threshold
            if sensor_measurements[-1][1] > temperature_alarm:
                QMessageBox.warning(self,'Limit Exceeded','Temperature limit exceeded.')
            if sensor_measurements[-1][2] > humidity_alarm:
                QMessageBox.warning(self,'Limit Exceeded','Humidity limit exceeded.')
            
            # Wait before requesting next value
            time.sleep(1)

    def calculateStatistics(self):
        temperature = []
        humidity = []
        if len(sensor_measurements) > 10:
            x = 10
        else:
            x = len(sensor_measurements)
        for i in range(x):
            temperature.append(sensor_measurements[-i][1])
            humidity.append(sensor_measurements[-i][2])
        mean_temp = statistics.fmean(temperature)
        mean_hum = statistics.fmean(humidity)
        # Print values in the table
        if self.values.rowCount()>0:
            x = self.values.rowCount()
            for i in range(x):
                    self.values.removeRow(x-i-1)
        self.values.insertRow(self.values.rowCount())
        self.values.setItem(self.values.rowCount()-1, 0, QTableWidgetItem('Mean'))
        self.values.setItem(self.values.rowCount()-1, 1, QTableWidgetItem(str(round(mean_temp,4))))
        self.values.setItem(self.values.rowCount()-1, 2, QTableWidgetItem(str(round(mean_hum,4))))
        self.values.insertRow(self.values.rowCount())
        self.values.setItem(self.values.rowCount()-1, 0, QTableWidgetItem('Minimum'))
        self.values.setItem(self.values.rowCount()-1, 1, QTableWidgetItem(str(round(min(temperature),4))))
        self.values.setItem(self.values.rowCount()-1, 2, QTableWidgetItem(str(round(min(humidity),4))))
        self.values.insertRow(self.values.rowCount())
        self.values.setItem(self.values.rowCount()-1, 0, QTableWidgetItem('Maximum'))
        self.values.setItem(self.values.rowCount()-1, 1, QTableWidgetItem(str(round(max(temperature),4))))
        self.values.setItem(self.values.rowCount()-1, 2, QTableWidgetItem(str(round(max(humidity),4))))

    def setAlarms(self):
        # Read current values in the QTextEdit and save them
        temperature_alarm = int(self.temp_warning.toPlainText())
        humidity_alarm = int(self.humidity_warning.toPlainText())
        msgBox = QMessageBox()
        msg = 'Temperature Alarm set to ' + str(temperature_alarm) + ' and Humidity Alarm set to ' + str(humidity_alarm) + '.'
        msgBox.setWindowTitle('Alarms Set')
        msgBox.setText(msg)
        msgBox.exec()

    def closeAndExit(self):
        sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
