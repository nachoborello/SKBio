# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/nacho/colegio/base de datos/asado manager/SKBio/SKBio.ui'
#
# Created: Mon Aug  4 08:51:05 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(521, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.principal = QtGui.QTabWidget(self.centralwidget)
        self.principal.setGeometry(QtCore.QRect(0, 0, 521, 561))
        self.principal.setObjectName(_fromUtf8("principal"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.comboBox = QtGui.QComboBox(self.tab_1)
        self.comboBox.setEnabled(True)
        self.comboBox.setGeometry(QtCore.QRect(353, 130, 141, 27))
        self.comboBox.setAccessibleName(_fromUtf8(""))
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setEditable(True)
        self.comboBox.setModelColumn(0)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label_4 = QtGui.QLabel(self.tab_1)
        self.label_4.setGeometry(QtCore.QRect(285, 136, 91, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton = QtGui.QPushButton(self.tab_1)
        self.pushButton.setGeometry(QtCore.QRect(350, 20, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_5 = QtGui.QLabel(self.tab_1)
        self.label_5.setGeometry(QtCore.QRect(20, 136, 91, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_3 = QtGui.QLineEdit(self.tab_1)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 130, 113, 27))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.tableWidget = QtGui.QTableWidget(self.tab_1)
        self.tableWidget.setGeometry(QtCore.QRect(20, 180, 331, 321))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.pushButton_2 = QtGui.QPushButton(self.tab_1)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 250, 98, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_4 = QtGui.QPushButton(self.tab_1)
        self.pushButton_4.setGeometry(QtCore.QRect(380, 310, 98, 27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.comboBox_2 = QtGui.QComboBox(self.tab_1)
        self.comboBox_2.setEnabled(True)
        self.comboBox_2.setGeometry(QtCore.QRect(40, 20, 211, 27))
        self.comboBox_2.setAccessibleName(_fromUtf8(""))
        self.comboBox_2.setAutoFillBackground(False)
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setModelColumn(0)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.principal.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tableWidget_2 = QtGui.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 40, 461, 451))
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.principal.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tableWidget_3 = QtGui.QTableWidget(self.tab_3)
        self.tableWidget_3.setGeometry(QtCore.QRect(10, 121, 501, 391))
        self.tableWidget_3.setObjectName(_fromUtf8("tableWidget_3"))
        self.tableWidget_3.setColumnCount(4)
        self.tableWidget_3.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        self.label_8 = QtGui.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(330, 20, 161, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_6 = QtGui.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(40, 20, 161, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(40, 80, 161, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_9 = QtGui.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(330, 80, 161, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.principal.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.tableWidget_4 = QtGui.QTableWidget(self.tab_4)
        self.tableWidget_4.setGeometry(QtCore.QRect(5, 101, 511, 411))
        self.tableWidget_4.setObjectName(_fromUtf8("tableWidget_4"))
        self.tableWidget_4.setColumnCount(4)
        self.tableWidget_4.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        self.pushButton_3 = QtGui.QPushButton(self.tab_4)
        self.pushButton_3.setGeometry(QtCore.QRect(397, 30, 111, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.principal.addTab(self.tab_4, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 521, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.principal.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_4.setText(_translate("MainWindow", "Nombre", None))
        self.pushButton.setText(_translate("MainWindow", "Nuevo", None))
        self.label_5.setText(_translate("MainWindow", "Paga   $", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Paga", None))
        self.pushButton_2.setText(_translate("MainWindow", "Agregar", None))
        self.pushButton_4.setText(_translate("MainWindow", "Borrar", None))
        self.principal.setTabText(self.principal.indexOf(self.tab_1), _translate("MainWindow", "Principal", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Direccion", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Fecha", None))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Monto Total", None))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Monto/persona", None))
        self.principal.setTabText(self.principal.indexOf(self.tab_2), _translate("MainWindow", "Historial", None))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre", None))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Pone", None))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Saca", None))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Pendiente", None))
        self.label_8.setText(_translate("MainWindow", "Monto por persona", None))
        self.label_6.setText(_translate("MainWindow", "Monto Total", None))
        self.label_7.setText(_translate("MainWindow", "------------------", None))
        self.label_9.setText(_translate("MainWindow", "--------------------", None))
        self.principal.setTabText(self.principal.indexOf(self.tab_3), _translate("MainWindow", "Totales", None))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre", None))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Direccion", None))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Telefono", None))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Deuda", None))
        self.pushButton_3.setText(_translate("MainWindow", "ver deudas", None))
        self.principal.setTabText(self.principal.indexOf(self.tab_4), _translate("MainWindow", "Personas", None))


