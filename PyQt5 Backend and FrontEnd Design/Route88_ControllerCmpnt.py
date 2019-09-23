# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Route88_ControllerCmpnt.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Route88_Controller_Window(object):
    def setupUi(self, Route88_Controller_Window):
        Route88_Controller_Window.setObjectName("Route88_Controller_Window")
        Route88_Controller_Window.setWindowModality(QtCore.Qt.ApplicationModal)
        Route88_Controller_Window.resize(671, 440)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Route88_Controller_Window.sizePolicy().hasHeightForWidth())
        Route88_Controller_Window.setSizePolicy(sizePolicy)
        Route88_Controller_Window.setMinimumSize(QtCore.QSize(671, 440))
        Route88_Controller_Window.setMaximumSize(QtCore.QSize(671, 440))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(False)
        font.setWeight(50)
        Route88_Controller_Window.setFont(font)
        Route88_Controller_Window.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Route88_Controller_Window.setTabletTracking(False)
        Route88_Controller_Window.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Route88_Controller_Window.setWindowTitle("Route88 System | Controller Menu")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("IcoDisplay/r_88.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Route88_Controller_Window.setWindowIcon(icon)
        Route88_Controller_Window.setToolTip("")
        Route88_Controller_Window.setWhatsThis("")
        Route88_Controller_Window.setStyleSheet("")
        Route88_Controller_Window.setSizeGripEnabled(True)
        Route88_Controller_Window.setModal(True)
        self.GroupContainer_StaffAccount = QtWidgets.QGroupBox(Route88_Controller_Window)
        self.GroupContainer_StaffAccount.setGeometry(QtCore.QRect(9, 116, 653, 311))
        self.GroupContainer_StaffAccount.setTitle("")
        self.GroupContainer_StaffAccount.setObjectName("GroupContainer_StaffAccount")
        self.StatusLabel = QtWidgets.QLabel(self.GroupContainer_StaffAccount)
        self.StatusLabel.setGeometry(QtCore.QRect(10, 280, 641, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.StatusLabel.setFont(font)
        self.StatusLabel.setObjectName("StatusLabel")
        self.groupBox = QtWidgets.QGroupBox(self.GroupContainer_StaffAccount)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 361, 261))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.GroupContainer_PassCred_2 = QtWidgets.QGroupBox(self.groupBox)
        self.GroupContainer_PassCred_2.setGeometry(QtCore.QRect(10, 30, 341, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GroupContainer_PassCred_2.sizePolicy().hasHeightForWidth())
        self.GroupContainer_PassCred_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.GroupContainer_PassCred_2.setFont(font)
        self.GroupContainer_PassCred_2.setFlat(False)
        self.GroupContainer_PassCred_2.setObjectName("GroupContainer_PassCred_2")
        self.user_StaffName = QtWidgets.QLabel(self.GroupContainer_PassCred_2)
        self.user_StaffName.setGeometry(QtCore.QRect(10, 30, 321, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.user_StaffName.setFont(font)
        self.user_StaffName.setObjectName("user_StaffName")
        self.GroupContainer_PassCred = QtWidgets.QGroupBox(self.groupBox)
        self.GroupContainer_PassCred.setGeometry(QtCore.QRect(10, 110, 341, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GroupContainer_PassCred.sizePolicy().hasHeightForWidth())
        self.GroupContainer_PassCred.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.GroupContainer_PassCred.setFont(font)
        self.GroupContainer_PassCred.setFlat(False)
        self.GroupContainer_PassCred.setObjectName("GroupContainer_PassCred")
        self.user_JobPosition = QtWidgets.QLabel(self.GroupContainer_PassCred)
        self.user_JobPosition.setGeometry(QtCore.QRect(10, 30, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.user_JobPosition.setFont(font)
        self.user_JobPosition.setObjectName("user_JobPosition")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 180, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.ctrl_UserLogout = QtWidgets.QPushButton(self.groupBox)
        self.ctrl_UserLogout.setGeometry(QtCore.QRect(230, 210, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ctrl_UserLogout.setFont(font)
        self.ctrl_UserLogout.setObjectName("ctrl_UserLogout")
        self.ctrl_ExitProgram = QtWidgets.QPushButton(self.groupBox)
        self.ctrl_ExitProgram.setGeometry(QtCore.QRect(90, 210, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ctrl_ExitProgram.setFont(font)
        self.ctrl_ExitProgram.setObjectName("ctrl_ExitProgram")
        self.groupBox_2 = QtWidgets.QGroupBox(self.GroupContainer_StaffAccount)
        self.groupBox_2.setGeometry(QtCore.QRect(390, 10, 251, 261))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 231, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.verticalLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(30)
        self.gridLayout.setObjectName("gridLayout")
        self.ctrl_POSSystem = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ctrl_POSSystem.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ctrl_POSSystem.sizePolicy().hasHeightForWidth())
        self.ctrl_POSSystem.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ctrl_POSSystem.setFont(font)
        self.ctrl_POSSystem.setObjectName("ctrl_POSSystem")
        self.gridLayout.addWidget(self.ctrl_POSSystem, 1, 0, 1, 1)
        self.ctrl_ManagementSystem = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ctrl_ManagementSystem.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ctrl_ManagementSystem.sizePolicy().hasHeightForWidth())
        self.ctrl_ManagementSystem.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ctrl_ManagementSystem.setFont(font)
        self.ctrl_ManagementSystem.setObjectName("ctrl_ManagementSystem")
        self.gridLayout.addWidget(self.ctrl_ManagementSystem, 0, 0, 1, 1)
        self.ctrl_AboutSystem = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ctrl_AboutSystem.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ctrl_AboutSystem.sizePolicy().hasHeightForWidth())
        self.ctrl_AboutSystem.setSizePolicy(sizePolicy)
        self.ctrl_AboutSystem.setObjectName("ctrl_AboutSystem")
        self.gridLayout.addWidget(self.ctrl_AboutSystem, 2, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Route88_Controller_Window)
        self.frame.setGeometry(QtCore.QRect(0, 0, 671, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(401, 101))
        self.frame.setMaximumSize(QtCore.QSize(671, 101))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(13, 71, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 71, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 71, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 71, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 71, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 71, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 71, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 71, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 71, 161))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.NoRole, brush)
        self.frame.setPalette(palette)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color:rgb(13, 71, 161)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(60, 10, 81, 81))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("IcoDisplay/r_88.ico"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(1, 1, 2, 2))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(160, 20, 381, 58))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.retranslateUi(Route88_Controller_Window)
        QtCore.QMetaObject.connectSlotsByName(Route88_Controller_Window)
        Route88_Controller_Window.setTabOrder(self.ctrl_UserLogout, self.ctrl_ManagementSystem)
        Route88_Controller_Window.setTabOrder(self.ctrl_ManagementSystem, self.ctrl_POSSystem)

    def retranslateUi(self, Route88_Controller_Window):
        _translate = QtCore.QCoreApplication.translate
        self.StatusLabel.setText(_translate("Route88_Controller_Window", "..."))
        self.groupBox.setTitle(_translate("Route88_Controller_Window", "Welcome Back, Staff~!"))
        self.GroupContainer_PassCred_2.setTitle(_translate("Route88_Controller_Window", "Staff Name"))
        self.user_StaffName.setText(_translate("Route88_Controller_Window", "..."))
        self.GroupContainer_PassCred.setTitle(_translate("Route88_Controller_Window", "Staff Job Position"))
        self.user_JobPosition.setText(_translate("Route88_Controller_Window", "..."))
        self.label_6.setText(_translate("Route88_Controller_Window", "Not this user? Please Log-out."))
        self.ctrl_UserLogout.setText(_translate("Route88_Controller_Window", "Log-out"))
        self.ctrl_ExitProgram.setText(_translate("Route88_Controller_Window", "Quit"))
        self.groupBox_2.setTitle(_translate("Route88_Controller_Window", "System Launcher"))
        self.ctrl_POSSystem.setText(_translate("Route88_Controller_Window", "Launch POS System"))
        self.ctrl_ManagementSystem.setText(_translate("Route88_Controller_Window", "Launch Management System"))
        self.ctrl_AboutSystem.setText(_translate("Route88_Controller_Window", "About This System"))
        self.label.setText(_translate("Route88_Controller_Window", "Route88 Bike Café"))
        self.label_2.setText(_translate("Route88_Controller_Window", "Point-Of-Sales and Data Management System"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Route88_Controller_Window = QtWidgets.QDialog()
    ui = Ui_Route88_Controller_Window()
    ui.setupUi(Route88_Controller_Window)
    Route88_Controller_Window.show()
    sys.exit(app.exec_())
