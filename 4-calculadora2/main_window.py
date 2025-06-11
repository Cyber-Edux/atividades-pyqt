# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(418, 297)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 24, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 3)

        self.clsPushButton = QPushButton(self.centralwidget)
        self.clsPushButton.setObjectName(u"clsPushButton")

        self.gridLayout.addWidget(self.clsPushButton, 0, 3, 1, 1)

        self.lbracketPushButton = QPushButton(self.centralwidget)
        self.lbracketPushButton.setObjectName(u"lbracketPushButton")

        self.gridLayout.addWidget(self.lbracketPushButton, 1, 0, 1, 1)

        self.rbracketPushButton = QPushButton(self.centralwidget)
        self.rbracketPushButton.setObjectName(u"rbracketPushButton")

        self.gridLayout.addWidget(self.rbracketPushButton, 1, 1, 1, 1)

        self.plusPushButton = QPushButton(self.centralwidget)
        self.plusPushButton.setObjectName(u"plusPushButton")

        self.gridLayout.addWidget(self.plusPushButton, 1, 3, 1, 1)

        self.pushButton1 = QPushButton(self.centralwidget)
        self.pushButton1.setObjectName(u"pushButton1")

        self.gridLayout.addWidget(self.pushButton1, 2, 0, 1, 1)

        self.pushButton2 = QPushButton(self.centralwidget)
        self.pushButton2.setObjectName(u"pushButton2")

        self.gridLayout.addWidget(self.pushButton2, 2, 1, 1, 1)

        self.pushButton3 = QPushButton(self.centralwidget)
        self.pushButton3.setObjectName(u"pushButton3")

        self.gridLayout.addWidget(self.pushButton3, 2, 2, 1, 1)

        self.pushButton7 = QPushButton(self.centralwidget)
        self.pushButton7.setObjectName(u"pushButton7")

        self.gridLayout.addWidget(self.pushButton7, 4, 0, 1, 1)

        self.pushButton9 = QPushButton(self.centralwidget)
        self.pushButton9.setObjectName(u"pushButton9")

        self.gridLayout.addWidget(self.pushButton9, 4, 2, 1, 1)

        self.pushButton0 = QPushButton(self.centralwidget)
        self.pushButton0.setObjectName(u"pushButton0")

        self.gridLayout.addWidget(self.pushButton0, 5, 1, 1, 1)

        self.mulPushButton = QPushButton(self.centralwidget)
        self.mulPushButton.setObjectName(u"mulPushButton")

        self.gridLayout.addWidget(self.mulPushButton, 3, 3, 1, 1)

        self.pushButton5 = QPushButton(self.centralwidget)
        self.pushButton5.setObjectName(u"pushButton5")

        self.gridLayout.addWidget(self.pushButton5, 3, 1, 1, 1)

        self.eqPushButton = QPushButton(self.centralwidget)
        self.eqPushButton.setObjectName(u"eqPushButton")

        self.gridLayout.addWidget(self.eqPushButton, 5, 3, 1, 1)

        self.pushButton6 = QPushButton(self.centralwidget)
        self.pushButton6.setObjectName(u"pushButton6")

        self.gridLayout.addWidget(self.pushButton6, 3, 2, 1, 1)

        self.minusPushButton = QPushButton(self.centralwidget)
        self.minusPushButton.setObjectName(u"minusPushButton")

        self.gridLayout.addWidget(self.minusPushButton, 2, 3, 1, 1)

        self.divPushButton = QPushButton(self.centralwidget)
        self.divPushButton.setObjectName(u"divPushButton")

        self.gridLayout.addWidget(self.divPushButton, 4, 3, 1, 1)

        self.pushButton4 = QPushButton(self.centralwidget)
        self.pushButton4.setObjectName(u"pushButton4")

        self.gridLayout.addWidget(self.pushButton4, 3, 0, 1, 1)

        self.pushButton8 = QPushButton(self.centralwidget)
        self.pushButton8.setObjectName(u"pushButton8")

        self.gridLayout.addWidget(self.pushButton8, 4, 1, 1, 1)

        self.powPushButton = QPushButton(self.centralwidget)
        self.powPushButton.setObjectName(u"powPushButton")

        self.gridLayout.addWidget(self.powPushButton, 1, 2, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 24, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 418, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculadora", None))
        self.clsPushButton.setText(QCoreApplication.translate("MainWindow", u"limpar", None))
        self.lbracketPushButton.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.rbracketPushButton.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.plusPushButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.mulPushButton.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.pushButton5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.eqPushButton.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pushButton6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.minusPushButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.divPushButton.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.pushButton4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.powPushButton.setText(QCoreApplication.translate("MainWindow", u"**", None))
    # retranslateUi

