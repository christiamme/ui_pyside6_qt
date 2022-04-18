################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(818, 605)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 541, 531))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.values = QTableWidget(self.horizontalLayoutWidget)
        if (self.values.columnCount() < 3):
            self.values.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.values.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.values.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.values.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.values.setObjectName("values")

        self.horizontalLayout.addWidget(self.values)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(560, 10, 231, 531))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.current_sensor = QPushButton(self.verticalLayoutWidget)
        self.current_sensor.setObjectName("current_sensor")

        self.verticalLayout.addWidget(self.current_sensor)

        self.next_10 = QPushButton(self.verticalLayoutWidget)
        self.next_10.setObjectName("next_10")

        self.verticalLayout.addWidget(self.next_10)

        self.calculate = QPushButton(self.verticalLayoutWidget)
        self.calculate.setObjectName("calculate")

        self.verticalLayout.addWidget(self.calculate)

        self.set_alarm = QPushButton(self.verticalLayoutWidget)
        self.set_alarm.setObjectName("set_alarm")

        self.verticalLayout.addWidget(self.set_alarm)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.label.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.label)

        self.temp_warning = QTextEdit(self.verticalLayoutWidget)
        self.temp_warning.setObjectName("temp_warning")
        self.temp_warning.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temp_warning.sizePolicy().hasHeightForWidth())
        self.temp_warning.setSizePolicy(sizePolicy)
        self.temp_warning.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.temp_warning)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.label_2)

        self.humidity_warning = QTextEdit(self.verticalLayoutWidget)
        self.humidity_warning.setObjectName("humidity_warning")
        sizePolicy.setHeightForWidth(self.humidity_warning.sizePolicy().hasHeightForWidth())
        self.humidity_warning.setSizePolicy(sizePolicy)
        self.humidity_warning.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout.addWidget(self.humidity_warning)

        self.closegui = QPushButton(self.verticalLayoutWidget)
        self.closegui.setObjectName("closegui")

        self.verticalLayout.addWidget(self.closegui)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 818, 30))
        self.menuSensor_Data = QMenu(self.menubar)
        self.menuSensor_Data.setObjectName("menuSensor_Data")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSensor_Data.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        ___qtablewidgetitem = self.values.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", "Time", None));
        ___qtablewidgetitem1 = self.values.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", "Temperature", None));
        ___qtablewidgetitem2 = self.values.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", "Humidity", None));
        self.current_sensor.setText(QCoreApplication.translate("MainWindow", "Read current", None))
        self.next_10.setText(QCoreApplication.translate("MainWindow", "Read next 10", None))
        self.calculate.setText(QCoreApplication.translate("MainWindow", "Calculate", None))
        self.set_alarm.setText(QCoreApplication.translate("MainWindow", "Set Alarms", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "Temperature Warning", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", "Humidity Warning", None))
        self.closegui.setText(QCoreApplication.translate("MainWindow", "Exit", None))
        self.menuSensor_Data.setTitle(QCoreApplication.translate("MainWindow", "Sensor Data", None))
    # retranslateUi
