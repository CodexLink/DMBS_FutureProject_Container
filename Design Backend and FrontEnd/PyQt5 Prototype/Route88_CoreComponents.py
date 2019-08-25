'''
    Filename: Route88_CoreFunc.py - Route 88 POS and Inventory System Core Functions
    Project File: Route88 POS and Inventory System
    Initially Created by Janrey Licas
    GUI Framework: PyQt5
    Github: https://github.com/CodexLink/DMBS_Route88_POSSystem

    Members:    Janrey Licas "CodexLink" - https://github.com/CodexLink
                Charles Ian Mascarenas "ci-mascarenas" - https://github.com/ci-mascarenas
                Jan Patrick Moreno "jaypeemrn" - https://github.com/jaypeemrn
                Brenda Hernandez "imbrendzzz" - https://github.com/imbrendzzz

    Multi-Level Inheritance Method of Application Architecture:
        -> 
    Core Component Structure:
        Class Route88_TechnicalCore()
            Methods:
                -> __init__()
        Class Route88_LoginCore()
            Methods:
                -> __init__()
                -> <ClassShortName>_LoadUIElement_Explicit
                -> <ClassShortName>_RunFuncAfterRender
        Class Route88_InventoryCore()
            Methods:
                -> __init__()
                -> <ClassShortName>_LoadUIElement_Explicit
                -> <ClassShortName>_RunFuncAfterRender
        Class Route88_POSCore()
            Methods:
                -> __init__()
                -> <ClassShortName>_LoadUIElement_Explicit
                -> <ClassShortName>_RunFuncAfterRender
    
    Legends:
        __init__() -> Class Initializers, Possibly Constructors
        <ClassShortName>_LoadUIElement_Explicit -> Load Extra Elements from 'That' UI
            > This was implemented to ensure that changes from the UI file will not affect any additional elements that we just manually added which cannot be initiated with Qt Designer, this would result to extra elements remains whatver UI file changes after generating using 'pyuic5' module.
        <ClassShortName>_RunFuncAfterRender -> Condition, Must Be After setupUi()
            > This was implemented right after setupUi(). Because, we have to initialize every value from the database which would then be shown after UI has been render. So that when the engine initiates .show(). All values is already there. So in sort, setup Values and Elements.
'''

from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtMultimedia import QSound
import MySQLdb as MySQL
import sys
from os import system as sysCmdArgumentHandler
from Route88_LoginForm import Ui_Route88_LoginWindow
from Route88_InventorySystem import Ui_Route88_InventorySystemView 
#from Route88_POSSystem import ???

# This class contains all technical function that would be used by these multiple class of multiple window.
class Route88_TechnicalCore(object):
    def __init__(self, Parent=None):
        super().__init__()

    # MySQL Mainstream Functions, Functions That Requires Calling MySQLdb Library
    # Initialize MySQL Server Twice, One for Login and Last.... ???
    def MySQL_ConnectDatabase(self, HostServerIP='localhost', SQL_UCredentials='root', SQL_PCredential='', SQLDatabase_Target='Route88_Staff'):
        try:
            self.MySQLDataWire = MySQL.connect(host=HostServerIP, user=SQL_UCredentials, passwd=SQL_PCredential, db=SQLDatabase_Target)
            print('MySQL Database Connection Attempt: User {0} is now logged as {1} with Database Role of {2}.'.format('???', SQL_UCredentials, '???'))
        except MySQL.OperationalError as MySQL_ErrorMessage:
            self.StatusLabel.setText("Database Error: Cannot Connect to the SQL Database. Please restart.")
            print(MySQL_ErrorMessage)

    # Sets CursorType for Iteration which outputs the following CursorType
    def MySQL_CursorSet(self, CursorType=None):
        try:
            self.MySQLDataWireCursor = self.MySQLDataWire.cursor(CursorType)
        except (Exception, MySQL.OperationalError) as CursorErrMsg:
            print(CursorErrMsg)

class Route88_LoginCore(Ui_Route88_LoginWindow, Route88_TechnicalCore):
    # Class Initializer, __init__
    def __init__(self, Parent=None):
        super(Route88_LoginCore, self).__init__(Parent=Parent)
        '''
            LoginWindow is Not Initialized / Seperate as a Function for Initialization.
                Note: The reason why we did this is because I don't things to be more complicated as it should be.
                So that when my other members start to read my code, it is exactly stated here that we want first to initialize LoginWindow
                other than anything that they thought, 'what the hell is this argument that you pass?'
                ~ All other window will be seperately initialized...
        '''
        #self.Route88_LoginWindow = Ui_Route88_LoginWindow()
        #self.Login_TechnicalCoreHandler = Route88_TechnicalCore()

        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('IcoDisplay/r_88.ico'))

        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowShadeButtonHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        # Button Binds for Window 'Route88_LoginForm'
        self.UserAcc_Password.returnPressed.connect(self.UserAcc_SubmitData.click)
        self.UserAcc_SubmitData.clicked.connect(self.LoginForm_DataSubmission)
        #Run The Following Functions for Initializing User Data @ Window 'Route88_LoginForm'

        self.LoginForm_RunFuncAfterRender()
    # Technical Functions
    # Load Function After UI Rendering.
    def LoginForm_RunFuncAfterRender(self):
        try:
            self.MySQL_ConnectDatabase()
            self.MySQL_CursorSet(MySQL.cursors.DictCursor)
            self.LoginForm_ParseUserEnlisted()
        except Exception as ErrorHandler:
            print(ErrorHandler)

    #Route88_LoginForm UI Window Functions - StartPoint
    def LoginForm_ParseUserEnlisted(self):
        try:
            currentRow = 0
            self.MySQL_CursorSet(MySQL.cursors.DictCursor)
            self.MySQLDataWireCursor.execute("SELECT * FROM Employees")
            UserDataTable = self.MySQLDataWireCursor.fetchall()

            for UserData in UserDataTable:
                self.UserAcc_Enlisted.setRowCount(currentRow + 1)
                self.UserAcc_Enlisted.setItem(currentRow, 0, QtWidgets.QTableWidgetItem('{0}, {1}'.format(UserData['lname'], UserData['fname'])))
                self.UserColumn_1 = self.UserAcc_Enlisted.item(currentRow, 0)
                self.UserColumn_1.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UserAcc_Enlisted.setItem(currentRow, 1, QtWidgets.QTableWidgetItem(UserData['JobPosition']))
                self.UserColumn_2 = self.UserAcc_Enlisted.item(currentRow, 1)
                self.UserColumn_2.setTextAlignment(QtCore.Qt.AlignCenter)
                currentRow += 1

            self.StatusLabel.setText("Database Loaded: Ready!")

        except MySQL.OperationalError as LoginQueryErrorMsg:
            print('MySQL.OperationalError -> {0}'.format(str(LoginQueryErrorMsg)))
            self.StatusLabel.setText("Database Error: Failed to Load User Data. Please restart the program.")

    def LoginForm_DataSubmission(self):
        try:
            self.MySQL_CursorSet(None)
            RowIndexSelected = self.UserAcc_Enlisted.selectionModel().selectedRows()
            for RowIndexQuery in sorted(RowIndexSelected):
                QueryReturn = self.MySQLDataWireCursor.execute("SELECT fname, lname FROM Employees WHERE concat(lname, ', ', fname) = %s AND password = %s", (
                    RowIndexQuery.data(), self.UserAcc_Password.text()))
                # After query we need to check if QueryReturn contains non-zero values. If it contains non-zero we proceed. Else not...

                # We need to store the credentials that is equalled to what we expect.
                if QueryReturn:
                    self.StatusLabel.setText("Login Success: Credential Input Matched!")
                    QSound.play("SysSounds/LoginSuccessNotify.wav")
                    QtTest.QTest.qWait(1500)
                    self.StatusLabel.setText("Successfully Logged in as ...".format("Unknown User..."))
                    QtTest.QTest.qWait(1500)
                    self.MySQLDataWire.close() # Reconnect to Anothe SQ: Usage with Specific User Parameters
                    self.close()
                    self.Route88_InventoryInstance = Route88_InventoryCore()
                    self.Route88_InventoryInstance.show()
                else:
                    self.StatusLabel.setText("Login Error: Credential Input Not Matched! Check your Password!")
                    QSound.play("SysSounds/LoginFailedNotify.wav")

        except Exception as LoginSubmissionErrorMsg:
            print(LoginSubmissionErrorMsg)
            self.StatusLabel.setText(str(LoginSubmissionErrorMsg))
            QSound.play("SysSounds/LoginFailedNotify.wav")
    # Route88_LoginForm UI Window Functions - EndPoint


class Route88_InventoryCore(Ui_Route88_InventorySystemView, Route88_TechnicalCore):
    def __init__(self, Parent=None):
        super(Route88_InventoryCore, self).__init__(Parent=Parent)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowShadeButtonHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.CustomizeWindowHint)
        self.setupUi(self)
        self.InventorySys_LoadUIElement_Explicit()
        self.setWindowIcon(QtGui.QIcon('IcoDisplay/r_88.ico'))
        # Button Binds for Window 'Route88_InventoryDesign'
        # > Search Query Binds
        self.Query_ValueToSearch.textChanged.connect(self.InventorySys_SearchVal)
        self.SearchPattern_ExactOpt.clicked.connect(self.InventorySys_PatternEnable)
        self.SearchPattern_ContainOpt.clicked.connect(self.InventorySys_PatternEnable)
        # > Staff Action Binds 
        self.StaffAct_Add.clicked.connect(self.InventorySys_AddEntry)
        self.StaffAct_Edit.clicked.connect(self.InventorySys_EditEntry_Selected)
        self.StaffAct_Delete.clicked.connect(self.InventorySys_DeleteEntry_Selected)
        self.StaffAct_RefreshData.clicked.connect(self.InventorySys_RefreshData)
        self.StaffAct_ResetView.clicked.connect(self.InventorySys_ResetGridView)
    
        self.InventorySys_RunFuncAfterRender() #Run This Function After UI Initialization

        #Function Definitions for Route88_InventoryDesign
        



    def InventorySys_LoadUIElement_Explicit(self):
    
        self.InventoryStatus = QtWidgets.QStatusBar()
        self.InventoryStatus.showMessage("asdhoiasdhoiasdhjoiasdjoi")
        self.setStatusBar(self.InventoryStatus)

    def InventorySys_RunFuncAfterRender(self):
        try: 
            self.MySQL_ConnectDatabase()
            self.MySQL_CursorSet(MySQL.cursors.DictCursor)
            self.InventorySys_LoadData()
        except (Exception, MySQL.OperationalError) as FunctionErrorMsg:
            self.InventoryStatus.showMessage('Application Error: {0}'.format(FunctionErrorMsg))
            print('[Exception Thrown @ InventorySys_RunFuncAfterRender] -> {0}'.format(FunctionErrorMsg))

    def InventorySys_LoadData(self):
        try:
            #Setups
            self.MySQLDataWireCursor.execute("DESCRIBE Employees")
            ColumnDataFetch = self.MySQLDataWireCursor.fetchall()
            self.MySQLDataWireCursor.execute("SELECT")
            InventoryDataFetch = self.MySQLDataWireCursor.fetchall()
            # Fill Query_ColumnOpt First.
            for ColumnData in ColumnDataFetch:
                self.Query_ColumnOpt.addItem(str(ColumnData['Field']))
            # Fill Inventory Menu
            for InventoryData in InventoryDataFetch:
                pass
            

        except (Exception, MySQL.OperationalError) as FunctionErrorMsg:
            self.InventoryStatus.showMessage('Application Error: {0}'.format(FunctionErrorMsg))
            print('[Exception Thrown @ InventorySys_LoadData] -> {0}'.format(FunctionErrorMsg))

    # Interactive Button to Function
    # Searcb Query Functions
    def InventorySys_SearchVal(self): # This function is fired every time there will be changes on the QLineEdit -> Query_ValueToSearch
        pass
    
    def InventorySys_PatternEnable(self, BoolPropertyToListDown):
        pass
    # Staff Action Functions
    def InventorySys_AddEntry(self):
        pass
    def InventorySys_EditEntry_Selected(self):
        pass
    def InventorySys_DeleteEntry_Selected(self):
        pass
    def InventorySys_RefreshData(self):

        pass
    def InventorySys_ResetGridView(self):
        pass
    # Event Handlers
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F4 and (event.modifiers() & QtCore.Qt.AltModifier):
            print("EventKeyPressed: ALT F4")
            event.ignore()
        if event.key() == QtCore.Qt.Key_Space:
            print("EventKeyPressed: Space")

# Literal Procedural Programming Part
if __name__ == "__main__":
    sysCmdArgumentHandler('CLS') # Clear Output Buffer so we can debug with dignity.
    print('[Application App Startup] Route88_Core Application Version 0, Debug Output')
    app = QtWidgets.QApplication(sys.argv)
    Route88_Instance = Route88_LoginCore()
    Route88_Instance.show()
    sys.exit(app.exec_())
    #print('[Application Shutdown] Terminating PyQt5 Engine...')