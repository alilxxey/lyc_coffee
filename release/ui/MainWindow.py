from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMainWindow
from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(701, 597)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(30, 20, 621, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 611, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_add_film = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_add_film.setObjectName("btn_add_film")
        self.horizontalLayout.addWidget(self.btn_add_film)
        self.btn_change_film = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_change_film.setObjectName("btn_change_film")
        self.horizontalLayout.addWidget(self.btn_change_film)
        self.btn_delete_film = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_delete_film.setObjectName("btn_delete_film")
        self.horizontalLayout.addWidget(self.btn_delete_film)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(5, 51, 601, 461))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tabWidget.addTab(self.widget, "")

        self.statusbar = QtWidgets.QStatusBar(Dialog)
        self.statusbar.setObjectName("statusbar")
        Dialog.setStatusBar(self.statusbar)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "кофеек"))
        self.tabWidget.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\">кофеек</p></body></html>"))
        self.btn_add_film.setText(_translate("Dialog", "Добавить кофе"))
        self.btn_change_film.setText(_translate("Dialog", "Изменить кофе"))
        self.btn_delete_film.setText(_translate("Dialog", "Удалить кофе"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("Dialog", "Tab 1"))
