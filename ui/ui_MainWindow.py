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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QTabWidget, QTableView, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(950, 731)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/images/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"font-family: Roboto;\n"
"font-size: 12pt;\n"
"")
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)

        self.viewOptionLayout = QHBoxLayout()
        self.viewOptionLayout.setObjectName(u"viewOptionLayout")
        self.viewOptionLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.dayRadioButton = QRadioButton(self.centralwidget)
        self.dayRadioButton.setObjectName(u"dayRadioButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.dayRadioButton.sizePolicy().hasHeightForWidth())
        self.dayRadioButton.setSizePolicy(sizePolicy2)
        self.dayRadioButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.dayRadioButton.setChecked(True)

        self.viewOptionLayout.addWidget(self.dayRadioButton)

        self.monthRadioButton = QRadioButton(self.centralwidget)
        self.monthRadioButton.setObjectName(u"monthRadioButton")
        sizePolicy2.setHeightForWidth(self.monthRadioButton.sizePolicy().hasHeightForWidth())
        self.monthRadioButton.setSizePolicy(sizePolicy2)

        self.viewOptionLayout.addWidget(self.monthRadioButton)

        self.yearRadioButton = QRadioButton(self.centralwidget)
        self.yearRadioButton.setObjectName(u"yearRadioButton")
        sizePolicy2.setHeightForWidth(self.yearRadioButton.sizePolicy().hasHeightForWidth())
        self.yearRadioButton.setSizePolicy(sizePolicy2)

        self.viewOptionLayout.addWidget(self.yearRadioButton)


        self.gridLayout_3.addLayout(self.viewOptionLayout, 1, 4, 1, 1)

        self.lastFetchedDateLabel = QLabel(self.centralwidget)
        self.lastFetchedDateLabel.setObjectName(u"lastFetchedDateLabel")

        self.gridLayout_3.addWidget(self.lastFetchedDateLabel, 1, 2, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet(u"padding-left: 10px")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_2, 0, 4, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.label_8, 1, 1, 1, 1)

        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy3)
        self.dateEdit.setStyleSheet(u"font-weight: bold;\n"
"")

        self.gridLayout_3.addWidget(self.dateEdit, 0, 2, 1, 1)

        self.insertTodayDateButton = QPushButton(self.centralwidget)
        self.insertTodayDateButton.setObjectName(u"insertTodayDateButton")
        sizePolicy2.setHeightForWidth(self.insertTodayDateButton.sizePolicy().hasHeightForWidth())
        self.insertTodayDateButton.setSizePolicy(sizePolicy2)
        icon1 = QIcon()
        icon1.addFile(u":/images/today_date.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.insertTodayDateButton.setIcon(icon1)
        self.insertTodayDateButton.setIconSize(QSize(24, 24))

        self.gridLayout_3.addWidget(self.insertTodayDateButton, 0, 3, 1, 1)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setPixmap(QPixmap(u":/images/edit_date.svg"))

        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy4)
        self.label_10.setMinimumSize(QSize(24, 24))
        self.label_10.setPixmap(QPixmap(u":/images/last_featched.svg"))
        self.label_10.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setStyleSheet(u"font-size: 14pt;\n"
"font-weight: bold;")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.emailEditLayout = QHBoxLayout()
        self.emailEditLayout.setObjectName(u"emailEditLayout")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 0))
        self.label_4.setMaximumSize(QSize(16777215, 16777215))

        self.emailEditLayout.addWidget(self.label_4)

        self.emailLineEdit = QLineEdit(self.centralwidget)
        self.emailLineEdit.setObjectName(u"emailLineEdit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.emailLineEdit.sizePolicy().hasHeightForWidth())
        self.emailLineEdit.setSizePolicy(sizePolicy5)
        self.emailLineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.emailLineEdit.setStyleSheet(u"padding:5px;")
        self.emailLineEdit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.emailEditLayout.addWidget(self.emailLineEdit)


        self.gridLayout.addLayout(self.emailEditLayout, 0, 0, 1, 1)

        self.passwordEditlayout = QHBoxLayout()
        self.passwordEditlayout.setObjectName(u"passwordEditlayout")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 0))
        self.label_5.setMaximumSize(QSize(16777215, 16777215))

        self.passwordEditlayout.addWidget(self.label_5)

        self.passwordLineEdit = QLineEdit(self.centralwidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setStyleSheet(u"padding:5px;")
        self.passwordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.passwordEditlayout.addWidget(self.passwordLineEdit)


        self.gridLayout.addLayout(self.passwordEditlayout, 1, 0, 1, 1)

        self.showPasswordButton = QPushButton(self.centralwidget)
        self.showPasswordButton.setObjectName(u"showPasswordButton")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.showPasswordButton.sizePolicy().hasHeightForWidth())
        self.showPasswordButton.setSizePolicy(sizePolicy6)
        self.showPasswordButton.setMaximumSize(QSize(36, 16777215))
        self.showPasswordButton.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/images/visibility_on.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.showPasswordButton.setIcon(icon2)
        self.showPasswordButton.setIconSize(QSize(24, 24))
        self.showPasswordButton.setCheckable(True)
        self.showPasswordButton.setChecked(False)

        self.gridLayout.addWidget(self.showPasswordButton, 1, 1, 1, 1)

        self.appIdEditLayout = QHBoxLayout()
        self.appIdEditLayout.setObjectName(u"appIdEditLayout")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(100, 0))

        self.appIdEditLayout.addWidget(self.label_6)

        self.appIdLineEdit = QLineEdit(self.centralwidget)
        self.appIdLineEdit.setObjectName(u"appIdLineEdit")
        self.appIdLineEdit.setStyleSheet(u"padding: 5px;")

        self.appIdEditLayout.addWidget(self.appIdLineEdit)


        self.gridLayout.addLayout(self.appIdEditLayout, 2, 0, 1, 1)

        self.appSecretEditLayout = QHBoxLayout()
        self.appSecretEditLayout.setObjectName(u"appSecretEditLayout")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(100, 0))

        self.appSecretEditLayout.addWidget(self.label_7)

        self.appSecretLineEdit = QLineEdit(self.centralwidget)
        self.appSecretLineEdit.setObjectName(u"appSecretLineEdit")
        self.appSecretLineEdit.setStyleSheet(u"padding:5px;")
        self.appSecretLineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.appSecretEditLayout.addWidget(self.appSecretLineEdit)


        self.gridLayout.addLayout(self.appSecretEditLayout, 3, 0, 1, 1)

        self.showAppSecretButton = QPushButton(self.centralwidget)
        self.showAppSecretButton.setObjectName(u"showAppSecretButton")
        self.showAppSecretButton.setMaximumSize(QSize(36, 16777215))
        self.showAppSecretButton.setStyleSheet(u"")
        self.showAppSecretButton.setIcon(icon2)
        self.showAppSecretButton.setIconSize(QSize(24, 24))
        self.showAppSecretButton.setCheckable(True)
        self.showAppSecretButton.setChecked(False)

        self.gridLayout.addWidget(self.showAppSecretButton, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.fetchDataButton = QPushButton(self.centralwidget)
        self.fetchDataButton.setObjectName(u"fetchDataButton")
        self.fetchDataButton.setStyleSheet(u"font-weight: bold;\n"
"padding: 5px;")

        self.verticalLayout.addWidget(self.fetchDataButton)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.horizontalHeader().setDefaultSectionSize(150)
        self.tableView.verticalHeader().setCascadingSectionResizes(True)

        self.verticalLayout.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 950, 33))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DeyeEconomy", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0431\u0435\u0440\u0456\u0442\u044c \u0434\u0430\u0442\u0443:", None))
        self.dayRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043d\u044c", None))
        self.monthRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0456\u0441\u044f\u0446\u044c", None))
        self.yearRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0456\u043a", None))
        self.lastFetchedDateLabel.setText(QCoreApplication.translate("MainWindow", u"dd.MM.yyyy hh:mm", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0440\u0438\u043c\u0430\u0442\u0438 \u0434\u0430\u043d\u0456 \u0437\u0430", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043d\u043d\u0454 \u043e\u043d\u043e\u0432\u043b\u0435\u043d\u043d\u044f: ", None))
        self.insertTodayDateButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0430\u0432\u0438\u0442\u0438 \u0441\u044c\u043e\u0433\u043e\u0434\u043d\u0456\u0448\u043d\u044e \u0434\u0430\u0442\u0443", None))
        self.label_9.setText("")
        self.label_10.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043b\u0430\u0448\u0442\u0443\u0432\u0430\u043d\u043d\u044f Deye Account", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.showPasswordButton.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"AppId:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"AppSecret:", None))
        self.showAppSecretButton.setText("")
        self.fetchDataButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0440\u0438\u043c\u0430\u0442\u0438 \u0434\u0430\u043d\u0456", None))
    # retranslateUi

