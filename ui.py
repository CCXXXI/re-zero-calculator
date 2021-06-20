# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1080, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1080, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1080, 720))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.browser.setGeometry(QtCore.QRect(140, 10, 931, 681))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.browser.setFont(font)
        self.browser.setObjectName("browser")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 121, 551))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_import_para = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_import_para.setObjectName("pushButton_import_para")
        self.verticalLayout.addWidget(self.pushButton_import_para)
        self.pushButton_import_xzq = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_import_xzq.setObjectName("pushButton_import_xzq")
        self.verticalLayout.addWidget(self.pushButton_import_xzq)
        self.pushButton_run = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_run.setEnabled(False)
        self.pushButton_run.setObjectName("pushButton_run")
        self.verticalLayout.addWidget(self.pushButton_run)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem)
        self.checkBox_mfq = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_mfq.setObjectName("checkBox_mfq")
        self.verticalLayout.addWidget(self.checkBox_mfq)
        self.label_mfq = QtWidgets.QLabel(self.layoutWidget)
        self.label_mfq.setObjectName("label_mfq")
        self.verticalLayout.addWidget(self.label_mfq)
        self.comboBox_mfq = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_mfq.setEnabled(False)
        self.comboBox_mfq.setMaxVisibleItems(39)
        self.comboBox_mfq.setObjectName("comboBox_mfq")
        self.comboBox_mfq.addItem("")
        self.comboBox_mfq.addItem("")
        self.comboBox_mfq.addItem("")
        self.comboBox_mfq.addItem("")
        self.comboBox_mfq.addItem("")
        self.comboBox_mfq.addItem("")
        self.comboBox_mfq.addItem("")
        self.comboBox_mfq.addItem("")
        self.comboBox_mfq.addItem("")
        self.comboBox_mfq.addItem("")
        self.comboBox_mfq.addItem("")
        self.comboBox_mfq.addItem("")
        self.comboBox_mfq.addItem("")
        self.comboBox_mfq.addItem("")
        self.comboBox_mfq.addItem("")
        self.verticalLayout.addWidget(self.comboBox_mfq)
        self.label_mfq_k = QtWidgets.QLabel(self.layoutWidget)
        self.label_mfq_k.setObjectName("label_mfq_k")
        self.verticalLayout.addWidget(self.label_mfq_k)
        self.comboBox_mfq_k = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_mfq_k.setEnabled(False)
        self.comboBox_mfq_k.setEditable(False)
        self.comboBox_mfq_k.setMaxVisibleItems(18)
        self.comboBox_mfq_k.setObjectName("comboBox_mfq_k")
        self.comboBox_mfq_k.addItem("")
        self.comboBox_mfq_k.addItem("")
        self.comboBox_mfq_k.addItem("")
        self.comboBox_mfq_k.addItem("")
        self.comboBox_mfq_k.addItem("")
        self.comboBox_mfq_k.addItem("")
        self.comboBox_mfq_k.addItem("")
        self.comboBox_mfq_k.addItem("")
        self.comboBox_mfq_k.addItem("")
        self.comboBox_mfq_k.addItem("")
        self.comboBox_mfq_k.addItem("")
        self.verticalLayout.addWidget(self.comboBox_mfq_k)
        self.label_mfq_num = QtWidgets.QLabel(self.layoutWidget)
        self.label_mfq_num.setObjectName("label_mfq_num")
        self.verticalLayout.addWidget(self.label_mfq_num)
        self.spinBox_mfq_num = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_mfq_num.setEnabled(False)
        self.spinBox_mfq_num.setMinimum(1)
        self.spinBox_mfq_num.setMaximum(12)
        self.spinBox_mfq_num.setProperty("value", 8)
        self.spinBox_mfq_num.setObjectName("spinBox_mfq_num")
        self.verticalLayout.addWidget(self.spinBox_mfq_num)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem1)
        self.label_xzq = QtWidgets.QLabel(self.layoutWidget)
        self.label_xzq.setObjectName("label_xzq")
        self.verticalLayout.addWidget(self.label_xzq)
        self.xzq_1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.xzq_1.setEnabled(True)
        self.xzq_1.setObjectName("xzq_1")
        self.verticalLayout.addWidget(self.xzq_1)
        self.xzq_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.xzq_2.setObjectName("xzq_2")
        self.verticalLayout.addWidget(self.xzq_2)
        self.xzq_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.xzq_3.setObjectName("xzq_3")
        self.verticalLayout.addWidget(self.xzq_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.bar = QtWidgets.QStatusBar(MainWindow)
        self.bar.setObjectName("bar")
        MainWindow.setStatusBar(self.bar)
        self.action_import = QtWidgets.QAction(MainWindow)
        self.action_import.setObjectName("action_import")
        self.action_export = QtWidgets.QAction(MainWindow)
        self.action_export.setObjectName("action_export")

        self.retranslateUi(MainWindow)
        self.comboBox_mfq_k.setCurrentIndex(5)
        self.pushButton_import_para.clicked.connect(MainWindow.import_para)
        self.pushButton_import_xzq.clicked.connect(MainWindow.import_xzq)
        self.pushButton_run.clicked.connect(MainWindow.run)
        self.checkBox_mfq.stateChanged["int"].connect(
            MainWindow.set_mfq_enabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton_import_para,
                               self.pushButton_import_xzq)
        MainWindow.setTabOrder(self.pushButton_import_xzq, self.pushButton_run)
        MainWindow.setTabOrder(self.pushButton_run, self.checkBox_mfq)
        MainWindow.setTabOrder(self.checkBox_mfq, self.comboBox_mfq)
        MainWindow.setTabOrder(self.comboBox_mfq, self.comboBox_mfq_k)
        MainWindow.setTabOrder(self.comboBox_mfq_k, self.spinBox_mfq_num)
        MainWindow.setTabOrder(self.spinBox_mfq_num, self.xzq_1)
        MainWindow.setTabOrder(self.xzq_1, self.xzq_2)
        MainWindow.setTabOrder(self.xzq_2, self.xzq_3)
        MainWindow.setTabOrder(self.xzq_3, self.browser)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Re:0手游装备推荐器&伤害计算器v3.0.1"))
        self.browser.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN"'
                ' "http://www.w3.org/TR/REC-html40/strict.dtd">\n<html><head><meta'
                ' name="qrichtext" content="1" /><style type="text/css">\np, li {'
                ' white-space: pre-wrap; }\n</style></head><body style="'
                " font-family:'Consolas'; font-size:9pt; font-weight:400;"
                ' font-style:normal;">\n<p style="-qt-paragraph-type:empty;'
                " margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;"
                ' -qt-block-indent:0; text-indent:0px; font-size:12pt;"><br'
                " /></p></body></html>",
            )
        )
        self.pushButton_import_para.setText(_translate("MainWindow", "指定角色数据"))
        self.pushButton_import_xzq.setText(_translate("MainWindow", "指定心之器数据"))
        self.pushButton_run.setText(_translate("MainWindow", "导入数据并计算"))
        self.checkBox_mfq.setText(_translate("MainWindow", "重塑魔法器"))
        self.label_mfq.setText(_translate("MainWindow", "指定魔法器"))
        self.comboBox_mfq.setItemText(0, _translate("MainWindow", "阴之水晶球"))
        self.comboBox_mfq.setItemText(1, _translate("MainWindow", "不蚀的箭矢"))
        self.comboBox_mfq.setItemText(2, _translate("MainWindow", "六面回音骰"))
        self.comboBox_mfq.setItemText(3, _translate("MainWindow", "女王的金器"))
        self.comboBox_mfq.setItemText(4, _translate("MainWindow", "倒流的沙漏"))
        self.comboBox_mfq.setItemText(5, _translate("MainWindow", "银质假面"))
        self.comboBox_mfq.setItemText(6, _translate("MainWindow", "石封之光"))
        self.comboBox_mfq.setItemText(7, _translate("MainWindow", "指引的胸针"))
        self.comboBox_mfq.setItemText(8, _translate("MainWindow", "龙纹手杖"))
        self.comboBox_mfq.setItemText(9, _translate("MainWindow", "附灵之戒"))
        self.comboBox_mfq.setItemText(10, _translate("MainWindow", "颤栗之匙"))
        self.comboBox_mfq.setItemText(11, _translate("MainWindow", "魔焰匕首"))
        self.comboBox_mfq.setItemText(12, _translate("MainWindow", "命运之刻"))
        self.comboBox_mfq.setItemText(13, _translate("MainWindow", "古怪的陶罐"))
        self.comboBox_mfq.setItemText(14, _translate("MainWindow", "沉睡的吊坠"))
        self.label_mfq_k.setText(_translate("MainWindow", "魔法器质量系数"))
        self.comboBox_mfq_k.setItemText(
            0, _translate("MainWindow", "100%(最好)"))
        self.comboBox_mfq_k.setItemText(
            1, _translate("MainWindow", "97.5%(S)"))
        self.comboBox_mfq_k.setItemText(
            2, _translate("MainWindow", "95%(S/A)"))
        self.comboBox_mfq_k.setItemText(
            3, _translate("MainWindow", "91.25%(A)"))
        self.comboBox_mfq_k.setItemText(
            4, _translate("MainWindow", "87.5%(A/B)"))
        self.comboBox_mfq_k.setItemText(
            5, _translate("MainWindow", "81.25%(B)"))
        self.comboBox_mfq_k.setItemText(
            6, _translate("MainWindow", "75%(B/C)"))
        self.comboBox_mfq_k.setItemText(7, _translate("MainWindow", "70%(C)"))
        self.comboBox_mfq_k.setItemText(
            8, _translate("MainWindow", "65%(C/D)"))
        self.comboBox_mfq_k.setItemText(
            9, _translate("MainWindow", "57.5%(D)"))
        self.comboBox_mfq_k.setItemText(
            10, _translate("MainWindow", "50%(最差)"))
        self.label_mfq_num.setText(_translate("MainWindow", "输出类词条数"))
        self.label_xzq.setText(_translate("MainWindow", "指定心之器"))
        self.xzq_1.setPlaceholderText(_translate("MainWindow", "剑圣的名义"))
        self.action_import.setText(_translate("MainWindow", "导入"))
        self.action_export.setText(_translate("MainWindow", "导出"))
