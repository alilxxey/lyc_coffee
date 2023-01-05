import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMainWindow
from PyQt5 import QtCore, QtWidgets

from ui.addEditCoffeeForm import Ui_add_coffee, Ui_DelWindow
from ui.MainWindow import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tabWidget.setTabText(0, 'Кофе')

        self.con = sqlite3.connect("../data/coffee.sqlite")
        self.load_films()

        self.btn_add_film.clicked.connect(self.add_film)
        self.btn_change_film.clicked.connect(self.change_film)
        self.btn_delete_film.clicked.connect(self.delete_film)

        self.addForm = None

    def load_films(self):
        res = self.con.cursor().execute(
            f"""SELECT id, variety, roast, seeds, description, price, volume FROM coffee
                ORDER BY id DESC;"""
        ).fetchall()
        self.tableWidget.setColumnCount(len(res[0]))
        self.tableWidget.setHorizontalHeaderLabels(
            ["ID", "Сорт", "Степень прожарки", "В зернах", "Описание", "Цена", "Объем"]
        )
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def add_film(self):
        self.addForm = AddWidgetFilm(self.con)
        self.addForm.show()

    def change_film(self):
        item = self.tableWidget.selectedItems()
        if not len(item) == 1:
            self.statusBar().showMessage('Нужно выбрать одну запись')
            return
        pk = self.tableWidget.item(item[0].row(), 0).text()
        _1 = self.tableWidget.item(item[0].row(), 1).text()
        _2 = self.tableWidget.item(item[0].row(), 2).text()
        _3 = self.tableWidget.item(item[0].row(), 3).text()
        _4 = self.tableWidget.item(item[0].row(), 4).text()
        _5 = self.tableWidget.item(item[0].row(), 5).text()
        _6 = self.tableWidget.item(item[0].row(), 6).text()
        self.addForm = AddWidgetFilm(self.con, id=pk, variety=_1, roast=_2, seeds=_3, description=_4, price=_5, volume=_6, pk=pk)
        self.addForm.show()

    def delete_film(self):
        item = self.tableWidget.selectedItems()
        if not len(item) == 1:
            self.statusBar().showMessage('Нужно выбрать одну запись')
            return
        pk = self.tableWidget.item(item[0].row(), 0).text()
        self.addForm = DelWidget(self.con, pk=pk, table='films')
        self.addForm.show()


class AddWidgetFilm(QMainWindow, Ui_add_coffee):
    def __init__(self, con, *, id=None, variety=None, roast=None, seeds=None, description=None, price=None, volume=None, pk=None):
        super().__init__()
        self.setupUi(self)
        self.con = con
        if id:
            self.IDinput.setValue(int(id))
            self.Varietyinput.setText(variety)
            self.roastinput.setValue(int(roast))
            self.seedinput.setValue(int(seeds))
            self.descinput.setText(description)
            self.priceinput.setValue(int(price))
            self.valueinput.setValue(int(volume))
            self.savebtn.setText('Изменить')
            self.setWindowTitle('Редактировать кофе')
            state = 'update'
        else:
            state = 'insert'
            self.savebtn.setText('Сохранить')
            self.setWindowTitle('Добавить кофе')

        self.savebtn.clicked.connect(lambda: self.add(state, pk))

    def add(self, state, pk):
        _id = self.IDinput.value()
        variety = self.Varietyinput.text()
        roast = self.roastinput.value()
        seeds = self.seedinput.value()
        description = self.descinput.text()
        price = self.priceinput.value()
        volume = self.valueinput.value()

        if state == 'insert':
            requset = (f"""INSERT INTO coffee(ID, variety, roast, seeds, description, price, volume)VALUES ({_id}, '{variety}', {roast}, {seeds}, '{description}', {price}, {volume});""")

        elif state == 'update':
            requset = (f"""UPDATE coffee
                       SET ID = {_id}, variety = "{variety}", roast = {roast}, seeds = {seeds}, description = "{description}", price = {price}, volume = {volume}
                       WHERE id = {pk}""")
        else:
            raise ValueError('Not valid SQL operation')
        self.con.cursor().execute(requset)
        self.con.commit()
        ex.load_films()
        self.hide()

class DelWidget(QMainWindow, Ui_DelWindow):
    def __init__(self, con, *, pk, table):
        super().__init__()
        self.con = con
        self.setupUi(self)
        self.radioButton.setChecked(True)
        self.pushButton.clicked.connect(lambda: self.confirm(pk, table))

    def confirm(self, pk, table):
        if not self.radioButton.isChecked():
            self.hide()
            return
        req = f"""DELETE FROM coffee
                      WHERE id = {pk}"""
        self.con.cursor().execute(req)
        self.con.commit()
        if table == 'films':
            ex.load_films()
        elif table == 'genres':
            ex.load_genres()
        self.hide()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())