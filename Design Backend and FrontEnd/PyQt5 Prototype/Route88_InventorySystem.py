# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Route88_InventorySystem.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Route88_InventorySystemView(QtWidgets.QMainWindow):
    def setupUi(self, Route88_InventorySystemView):
        Route88_InventorySystemView.setObjectName("Route88_InventorySystemView")
        Route88_InventorySystemView.setWindowModality(QtCore.Qt.ApplicationModal)
        Route88_InventorySystemView.resize(1068, 608)
        Route88_InventorySystemView.setMouseTracking(True)
        Route88_InventorySystemView.setFocusPolicy(QtCore.Qt.TabFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("IcoDisplay/r_88.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Route88_InventorySystemView.setWindowIcon(icon)
        Route88_InventorySystemView.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(Route88_InventorySystemView)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.Query_ColumnOpt = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Query_ColumnOpt.sizePolicy().hasHeightForWidth())
        self.Query_ColumnOpt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.Query_ColumnOpt.setFont(font)
        self.Query_ColumnOpt.setObjectName("Query_ColumnOpt")
        self.Query_ColumnOpt.addItem("")
        self.horizontalLayout_2.addWidget(self.Query_ColumnOpt)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.Query_ValueToSearch = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Query_ValueToSearch.sizePolicy().hasHeightForWidth())
        self.Query_ValueToSearch.setSizePolicy(sizePolicy)
        self.Query_ValueToSearch.setClearButtonEnabled(True)
        self.Query_ValueToSearch.setObjectName("Query_ValueToSearch")
        self.horizontalLayout_2.addWidget(self.Query_ValueToSearch)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.SearchPattern_ExactOpt = QtWidgets.QRadioButton(self.groupBox_4)
        self.SearchPattern_ExactOpt.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.SearchPattern_ExactOpt.setFont(font)
        self.SearchPattern_ExactOpt.setChecked(True)
        self.SearchPattern_ExactOpt.setAutoExclusive(True)
        self.SearchPattern_ExactOpt.setObjectName("SearchPattern_ExactOpt")
        self.horizontalLayout_5.addWidget(self.SearchPattern_ExactOpt)
        self.SearchPattern_ContainOpt = QtWidgets.QRadioButton(self.groupBox_4)
        self.SearchPattern_ContainOpt.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.SearchPattern_ContainOpt.setFont(font)
        self.SearchPattern_ContainOpt.setObjectName("SearchPattern_ContainOpt")
        self.horizontalLayout_5.addWidget(self.SearchPattern_ContainOpt)
        self.SearchPattern_ComboBox = QtWidgets.QComboBox(self.groupBox_4)
        self.SearchPattern_ComboBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchPattern_ComboBox.sizePolicy().hasHeightForWidth())
        self.SearchPattern_ComboBox.setSizePolicy(sizePolicy)
        self.SearchPattern_ComboBox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.SearchPattern_ComboBox.setFont(font)
        self.SearchPattern_ComboBox.setObjectName("SearchPattern_ComboBox")
        self.SearchPattern_ComboBox.addItem("")
        self.SearchPattern_ComboBox.addItem("")
        self.SearchPattern_ComboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.SearchPattern_ComboBox)
        self.horizontalLayout_6.addWidget(self.groupBox_4)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.InventoryView_Supplies = QtWidgets.QTableWidget(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        self.InventoryView_Supplies.setFont(font)
        self.InventoryView_Supplies.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.InventoryView_Supplies.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.InventoryView_Supplies.setAlternatingRowColors(True)
        self.InventoryView_Supplies.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.InventoryView_Supplies.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.InventoryView_Supplies.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.InventoryView_Supplies.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.InventoryView_Supplies.setShowGrid(True)
        self.InventoryView_Supplies.setGridStyle(QtCore.Qt.DashLine)
        self.InventoryView_Supplies.setCornerButtonEnabled(False)
        self.InventoryView_Supplies.setObjectName("InventoryView_Supplies")
        self.InventoryView_Supplies.setColumnCount(11)
        self.InventoryView_Supplies.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.InventoryView_Supplies.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.InventoryView_Supplies.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.InventoryView_Supplies.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.InventoryView_Supplies.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.InventoryView_Supplies.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.InventoryView_Supplies.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.InventoryView_Supplies.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.InventoryView_Supplies.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.InventoryView_Supplies.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.InventoryView_Supplies.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.InventoryView_Supplies.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.InventoryView_Supplies.setHorizontalHeaderItem(10, item)
        self.InventoryView_Supplies.verticalHeader().setVisible(True)
        self.InventoryView_Supplies.verticalHeader().setSortIndicatorShown(True)
        self.InventoryView_Supplies.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout.addWidget(self.InventoryView_Supplies)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.StaffAct_Add = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StaffAct_Add.sizePolicy().hasHeightForWidth())
        self.StaffAct_Add.setSizePolicy(sizePolicy)
        self.StaffAct_Add.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.StaffAct_Add.setFont(font)
        self.StaffAct_Add.setObjectName("StaffAct_Add")
        self.horizontalLayout_4.addWidget(self.StaffAct_Add)
        self.StaffAct_Edit = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StaffAct_Edit.sizePolicy().hasHeightForWidth())
        self.StaffAct_Edit.setSizePolicy(sizePolicy)
        self.StaffAct_Edit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.StaffAct_Edit.setFont(font)
        self.StaffAct_Edit.setObjectName("StaffAct_Edit")
        self.horizontalLayout_4.addWidget(self.StaffAct_Edit)
        self.StaffAct_Delete = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StaffAct_Delete.sizePolicy().hasHeightForWidth())
        self.StaffAct_Delete.setSizePolicy(sizePolicy)
        self.StaffAct_Delete.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.StaffAct_Delete.setFont(font)
        self.StaffAct_Delete.setObjectName("StaffAct_Delete")
        self.horizontalLayout_4.addWidget(self.StaffAct_Delete)
        self.StaffAct_RefreshData = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StaffAct_RefreshData.sizePolicy().hasHeightForWidth())
        self.StaffAct_RefreshData.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.StaffAct_RefreshData.setFont(font)
        self.StaffAct_RefreshData.setObjectName("StaffAct_RefreshData")
        self.horizontalLayout_4.addWidget(self.StaffAct_RefreshData)
        self.StaffAct_ResetView = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StaffAct_ResetView.sizePolicy().hasHeightForWidth())
        self.StaffAct_ResetView.setSizePolicy(sizePolicy)
        self.StaffAct_ResetView.setObjectName("StaffAct_ResetView")
        self.horizontalLayout_4.addWidget(self.StaffAct_ResetView)
        self.verticalLayout.addWidget(self.groupBox_2)
        Route88_InventorySystemView.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Route88_InventorySystemView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1068, 21))
        self.menubar.setObjectName("menubar")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuStaffs = QtWidgets.QMenu(self.menubar)
        self.menuStaffs.setObjectName("menuStaffs")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        Route88_InventorySystemView.setMenuBar(self.menubar)
        self.About_InfoSystem = QtWidgets.QAction(Route88_InventorySystemView)
        self.About_InfoSystem.setObjectName("About_InfoSystem")
        self.Staff_SwitchTo = QtWidgets.QAction(Route88_InventorySystemView)
        self.Staff_SwitchTo.setObjectName("Staff_SwitchTo")
        self.Staff_Manage = QtWidgets.QAction(Route88_InventorySystemView)
        self.Staff_Manage.setObjectName("Staff_Manage")
        self.Window_SwitchSystemView = QtWidgets.QAction(Route88_InventorySystemView)
        self.Window_SwitchSystemView.setObjectName("Window_SwitchSystemView")
        self.Window_Quit = QtWidgets.QAction(Route88_InventorySystemView)
        self.Window_Quit.setObjectName("Window_Quit")
        self.menuWindow.addAction(self.Window_SwitchSystemView)
        self.menuWindow.addAction(self.Window_Quit)
        self.menuStaffs.addAction(self.Staff_SwitchTo)
        self.menuStaffs.addAction(self.Staff_Manage)
        self.menuAbout.addAction(self.About_InfoSystem)
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuStaffs.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(Route88_InventorySystemView)
        QtCore.QMetaObject.connectSlotsByName(Route88_InventorySystemView)

    def retranslateUi(self, Route88_InventorySystemView):
        _translate = QtCore.QCoreApplication.translate
        Route88_InventorySystemView.setWindowTitle(_translate("Route88_InventorySystemView", "Route88 System | Inventory SystemView"))
        self.groupBox_3.setTitle(_translate("Route88_InventorySystemView", "Search Query"))
        self.label.setText(_translate("Route88_InventorySystemView", "By"))
        self.Query_ColumnOpt.setItemText(0, _translate("Route88_InventorySystemView", "<All Column>"))
        self.label_2.setText(_translate("Route88_InventorySystemView", "Look For"))
        self.Query_ValueToSearch.setPlaceholderText(_translate("Route88_InventorySystemView", "Value Search..."))
        self.groupBox_4.setTitle(_translate("Route88_InventorySystemView", "Search For Patterns Options"))
        self.SearchPattern_ExactOpt.setText(_translate("Route88_InventorySystemView", "Exact"))
        self.SearchPattern_ContainOpt.setText(_translate("Route88_InventorySystemView", "Contains"))
        self.SearchPattern_ComboBox.setItemText(0, _translate("Route88_InventorySystemView", "Between"))
        self.SearchPattern_ComboBox.setItemText(1, _translate("Route88_InventorySystemView", "Starting With"))
        self.SearchPattern_ComboBox.setItemText(2, _translate("Route88_InventorySystemView", "Ends With"))
        self.groupBox.setTitle(_translate("Route88_InventorySystemView", "Inventory View"))
        self.InventoryView_Supplies.setSortingEnabled(True)
        item = self.InventoryView_Supplies.verticalHeaderItem(0)
        item.setText(_translate("Route88_InventorySystemView", "1"))
        item = self.InventoryView_Supplies.horizontalHeaderItem(0)
        item.setText(_translate("Route88_InventorySystemView", "ItemCode"))
        item = self.InventoryView_Supplies.horizontalHeaderItem(1)
        item.setText(_translate("Route88_InventorySystemView", "SupplierCode"))
        item = self.InventoryView_Supplies.horizontalHeaderItem(2)
        item.setText(_translate("Route88_InventorySystemView", "Item Name"))
        item = self.InventoryView_Supplies.horizontalHeaderItem(3)
        item.setText(_translate("Route88_InventorySystemView", "Type"))
        item = self.InventoryView_Supplies.horizontalHeaderItem(4)
        item.setText(_translate("Route88_InventorySystemView", "Quantity"))
        item = self.InventoryView_Supplies.horizontalHeaderItem(5)
        item.setText(_translate("Route88_InventorySystemView", "Cost"))
        item = self.InventoryView_Supplies.horizontalHeaderItem(6)
        item.setText(_translate("Route88_InventorySystemView", "Supplier Name"))
        item = self.InventoryView_Supplies.horizontalHeaderItem(7)
        item.setText(_translate("Route88_InventorySystemView", "Expiry Date"))
        item = self.InventoryView_Supplies.horizontalHeaderItem(8)
        item.setText(_translate("Route88_InventorySystemView", "Menu Inclusion"))
        item = self.InventoryView_Supplies.horizontalHeaderItem(9)
        item.setText(_translate("Route88_InventorySystemView", "Data Created"))
        item = self.InventoryView_Supplies.horizontalHeaderItem(10)
        item.setText(_translate("Route88_InventorySystemView", "Last Modified"))
        self.groupBox_2.setTitle(_translate("Route88_InventorySystemView", "Staff Actions"))
        self.StaffAct_Add.setText(_translate("Route88_InventorySystemView", "Add Entry"))
        self.StaffAct_Edit.setText(_translate("Route88_InventorySystemView", "Edit / Modify Selected Entry"))
        self.StaffAct_Delete.setText(_translate("Route88_InventorySystemView", "Delete Entry"))
        self.StaffAct_RefreshData.setText(_translate("Route88_InventorySystemView", "Refresh Database"))
        self.StaffAct_ResetView.setText(_translate("Route88_InventorySystemView", "Reset Grid View"))
        self.menuWindow.setTitle(_translate("Route88_InventorySystemView", "Window"))
        self.menuStaffs.setTitle(_translate("Route88_InventorySystemView", "Staffs"))
        self.menuAbout.setTitle(_translate("Route88_InventorySystemView", "About"))
        self.About_InfoSystem.setText(_translate("Route88_InventorySystemView", "About This System..."))
        self.Staff_SwitchTo.setText(_translate("Route88_InventorySystemView", "Logout / Switch To..."))
        self.Staff_Manage.setText(_translate("Route88_InventorySystemView", "Manage Staffs..."))
        self.Window_SwitchSystemView.setText(_translate("Route88_InventorySystemView", "Switch System..."))
        self.Window_Quit.setText(_translate("Route88_InventorySystemView", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Route88_InventorySystemView = QtWidgets.QMainWindow()
    ui = Ui_Route88_InventorySystemView()
    ui.setupUi(Route88_InventorySystemView)
    Route88_InventorySystemView.show()
    sys.exit(app.exec_())
