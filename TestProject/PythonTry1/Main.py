#Standard module inclusions
import os
import os.path
import sys
import inspect
import time
import threading

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow,QTableWidgetItem, QTreeWidgetItem, QTreeWidget, QMessageBox


#App specific modules inclusions
from  MainWindow import *
from IdlFrmDebug import *
from IdlFrmSpoManager import *
from IdlFrmCliParser import *

#Deneme amaçlı thread sınıfı2
class TestThread2(QtCore.QThread):

    UpdaterSignal = QtCore.pyqtSignal(object,object)

    def __init__(self,prmThreadName="Default Thread Name"):
        QtCore.QThread.__init__(self)
        self.Thread1LocalCounter1=100
        self.ThreadName=prmThreadName
        

    def run(self):
        self.Thread1LocalCounter1=0
        while True:
            self.Thread1LocalCounter1+=1
            #TODO=Çok hızlı signal emit edildiğinde GUI Freeze oluyor. İyi ayarlanacak ve sabitlere konulacak..Ayrıca thread sayısına bağlı değişimi ölçülecek.
            #sleep olmadığı durumda freeze oluşuyor. Yada UI Refresh sıklığı signal handler slot da yapılabilir. Tüm threadler için ortak yapı için daha uygun olabilir.
            
            #time.sleep(0.000000000000000001) #AppDebugMan.DebugInfo yazdırılmadığı durumda bu değerde güzel çalışıyor.
            #time.sleep(0.007) #Tek thread de OK. AppDebugMan.DebugInfo yazdırıldığında, dosyaya yazmayınca gayet iyi, dosyaya yazdırınca da oldukça iyi çalışıyor.
            time.sleep(0.05) #İki thread de deneniyor.
            #ui.textEditDebug1.setText(str(Thread1LocalCounter1)) #burada kullanılamaz. Çünkü bu thread de yaratılmadı.
            #self.UpdaterSignal.emit("",self.Thread1LocalCounter1)
            #self.UpdaterSignal.emit(str(self.Thread1LocalCounter1)+" Değer1 from "+str(self.currentThreadId()))
            self.UpdaterSignal.emit(str(self.Thread1LocalCounter1),str(self.Thread1LocalCounter1)+" Değer1 from ThreadName="+self.ThreadName+" ThreadID="+str(int(self.currentThreadId())))
def on_data_ready(counter,data): #TODO=Benzer şekilde farklı threadlerin GUI yi bu yöntemle refresh/update etmesi denenecek.
    #global ui
    #global EditBoxSearch1
    #print data
    #if counter=="3":
    #    AppDebugMan.DebugInfo("Cx="+str(data))
    
    #Uncomment to see the logs in GUI AppDebugMan.DebugInfo("Cx="+str(data))
    #AppDebugMan.DebugInfo("Cx="+data)
    
    #print("Cx="+str(data))
    #ui.textEditDebug1.setText(str(data))
    EditBoxSearch1.setText(str(data))
    #EditBoxSearch1.setText(data)
    #AppMain.processEvents() #kombinasyonlu deneniyor. Çakılmaya yol açıyor.
#-------------------------------------------------------
# TEST STUB CODEs RANGE STARTs..
#-------------------------------------------------------
def TestStub_buttonAddRowClick():
    
    AddNewRowToGrid("XX1","DescX","IPx","LocationX","NOT Connected","N/A","Yes")
    return None
def TestStub_button2Click():
    global ui
    global tree
    global rootItem
    tree = ui.treeWidget1
    tree.setColumnCount(2)
    
    rootItem1 =  QTreeWidgetItem(tree)
    rootItem1.setText(0, "Root1")

    rootItem2 =  QTreeWidgetItem()
    rootItem2.setText(0, "Root2")

    #tree.addTopLevelItem(QTreeWidgetItem())
    tree.addTopLevelItem(rootItem2)

    #checkbox item add try STARTs....
    rootItem2.setFlags(rootItem2.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
    NewChildItemR2_x1 =  QTreeWidgetItem(rootItem2)
    NewChildItemR2_x1.setFlags(NewChildItemR2_x1.flags() | Qt.ItemIsUserCheckable)
    NewChildItemR2_x1.setText(0, "Childxxx")
    NewChildItemR2_x1.setText(1, "yyy")
    NewChildItemR2_x1.setCheckState(0, Qt.Unchecked)
    #checkbox item add try ENDs....


    #Add child items to Root1 Node
    NewChildItemR1_1 =  QTreeWidgetItem(rootItem1)
    NewChildItemR1_1.setText(0, "Oslo")
    NewChildItemR1_1.setText(1, "Yes") 

    #Add child items to Root1 Node
    NewChildItemR1_2 =  QTreeWidgetItem(rootItem1)
    NewChildItemR1_2.setText(0, "Kiev")
    NewChildItemR1_2.setText(1, "No") 

    #Add child items to Root1 Node
    NewChildItemR1_3 =  QTreeWidgetItem(rootItem1)
    NewChildItemR1_3.setText(0, "Moscowa")
    NewChildItemR1_3.setText(1, "Yes") 


    #Add child items to Root2 Node
    NewChildItemR2_1 =  QTreeWidgetItem(rootItem2)
    NewChildItemR2_1.setText(0, "Giresun")
    NewChildItemR2_1.setText(1, "No") 

    NewChildItemR2_2 =  QTreeWidgetItem(rootItem2)
    NewChildItemR2_2.setText(0, "Ordu")
    NewChildItemR2_2.setText(1, "Yes") 

    NewChildItemR2_3 =  QTreeWidgetItem(rootItem2)
    NewChildItemR2_3.setText(0, "Trabzon")
    NewChildItemR2_3.setText(1, "No") 

    #add child items to child items
    NewChildItemR1_1_1 =  QTreeWidgetItem(NewChildItemR1_1)
    NewChildItemR1_1_1.setText(0, "Osloya1")
    NewChildItemR1_1_1.setText(1, "No") 

    NewChildItemR1_1_2 =  QTreeWidgetItem(NewChildItemR1_1)
    NewChildItemR1_1_2.setText(0, "Osloya2")
    NewChildItemR1_1_2.setText(1, "Tuhaf2") 

    NewChildItemR1_1_1_1 =  QTreeWidgetItem(NewChildItemR1_1_1)
    NewChildItemR1_1_1_1.setText(0, "Osloya1.1")
    NewChildItemR1_1_1_1.setText(1, "Memleket2") 

    NewChildItemR1_1_1_2 =  QTreeWidgetItem(NewChildItemR1_1_1)
    NewChildItemR1_1_1_2.setText(0, "Osloya1.2")
    NewChildItemR1_1_1_2.setText(1, "Neresi2") 



    NewChildItemR2_1_1 =  QTreeWidgetItem(NewChildItemR2_1)
    NewChildItemR2_1_1.setText(0, "Espiye")
    NewChildItemR2_1_1.setText(1, "No") 

    NewChildItemR2_1_2 =  QTreeWidgetItem(NewChildItemR2_1)
    NewChildItemR2_1_2.setText(0, "Keşap")
    NewChildItemR2_1_2.setText(1, "Tuhaf") 

    NewChildItemR2_1_1_1 =  QTreeWidgetItem(NewChildItemR2_1_1)
    NewChildItemR2_1_1_1.setText(0, "Düzköy")
    NewChildItemR2_1_1_1.setText(1, "Memleket") 

    NewChildItemR2_1_1_2 =  QTreeWidgetItem(NewChildItemR2_1_1)
    NewChildItemR2_1_1_2.setText(0, "Gölköy")
    NewChildItemR2_1_1_2.setText(1, "Neresi") 

    return None

def TestStub_button2ClickExVersionDELETE():
    #----------------------------
    #open qss file
    fileStyle = open("StyleSheets\Adaptic\Adaptic.qss",'r')
    #fileStyle = open("StyleSheets\Combinear\Combinear.qss",'r')
    #fileStyle = open("StyleSheets\Darkeum\Darkeum.qss",'r')

    with fileStyle:
	    qss = fileStyle.read()
	    app.setStyleSheet(qss)
    #----------------------------

    return None
#Problemous:Doesn't refresh GUI timely
def SimTestAuto_ConnectDisconnectRun():
    global ui
    global AppMain
    tmpWaitTime=1

    MessageBox("Info","Simulated Run1 Shall Start")
    AppDebugMan.DebugInfo("SimTestAuto_Connecting[192.168.0.4")
    ClientConnectedGUIRefresh("192.168.0.4")
    ui.tableWidget1.repaint()
    time.sleep(tmpWaitTime)
    AppMain.processEvents()
    
    AppDebugMan.DebugInfo("SimTestAuto_Connecting[192.168.0.5")
    ClientConnectedGUIRefresh("192.168.0.5")
    ui.tableWidget1.repaint()
    time.sleep(tmpWaitTime)
    AppMain.processEvents()

    AppDebugMan.DebugInfo("SimTestAuto_Connecting[192.168.0.6")
    ClientConnectedGUIRefresh("192.168.0.6")
    ui.tableWidget1.repaint()
    AppMain.processEvents()
    time.sleep(tmpWaitTime)

    AppDebugMan.DebugInfo("SimTestAuto_Connecting[192.168.0.7")
    ClientConnectedGUIRefresh("192.168.0.7")
    ui.tableWidget1.repaint()
    AppMain.processEvents()
    time.sleep(tmpWaitTime)
    

    AppDebugMan.DebugInfo("SimTestAuto_Connecting[192.168.0.2")
    ClientConnectedGUIRefresh("192.168.0.2")
    ui.tableWidget1.repaint()
    time.sleep(tmpWaitTime)
    AppMain.processEvents()


    AppDebugMan.DebugInfo("SimTestAuto_DisConnecting[192.168.0.4")
    ClientDisConnectedGUIRefresh("192.168.0.4")
    ui.tableWidget1.repaint()
    time.sleep(tmpWaitTime)
    AppMain.processEvents()

    AppDebugMan.DebugInfo("SimTestAuto_DisConnecting[192.168.0.5")
    ClientDisConnectedGUIRefresh("192.168.0.5")
    ui.tableWidget1.repaint()
    time.sleep(tmpWaitTime)
    AppMain.processEvents()

    AppDebugMan.DebugInfo("SimTestAuto_DisConnecting[192.168.0.6")
    ClientDisConnectedGUIRefresh("192.168.0.6")
    ui.tableWidget1.repaint()
    time.sleep(tmpWaitTime)
    AppMain.processEvents()

    AppDebugMan.DebugInfo("SimTestAuto_DisConnecting[192.168.0.2")
    ClientDisConnectedGUIRefresh("192.168.0.2")
    ui.tableWidget1.repaint()
    time.sleep(tmpWaitTime)
    AppMain.processEvents()
    
    MessageBox("Info","Simulated Run1 Ended")

    return None
def SimTestAuto_ConnectDisconnectRunActionCall(prmStrIP,prmActionCode,prmWaitDuration):
    global ui
    if prmActionCode==1:
        AppDebugMan.DebugInfo("SimTestAuto_Connecting["+prmStrIP+"]")
        ClientConnectedGUIRefresh(prmStrIP)
    else:
        AppDebugMan.DebugInfo("SimTestAuto_DisConnecting["+prmStrIP+"]")
        ClientDisConnectedGUIRefresh(prmStrIP)

    ui.tableWidget1.repaint()
    time.sleep(prmWaitDuration)

    return None
def SimTestAuto_ConnectDisconnectRunV2():
    global ui
    tmpWaitTime=1
    
    MessageBox("Info","Simulated Run1 Shall Start")
    SimTestAuto_ConnectDisconnectRunActionCall("192.168.0.4",1,tmpWaitTime)
    SimTestAuto_ConnectDisconnectRunActionCall("192.168.0.5",1,tmpWaitTime)
    SimTestAuto_ConnectDisconnectRunActionCall("192.168.0.6",1,tmpWaitTime)
    SimTestAuto_ConnectDisconnectRunActionCall("192.168.0.2",1,tmpWaitTime)
    
    SimTestAuto_ConnectDisconnectRunActionCall("192.168.0.4",0,tmpWaitTime)
    SimTestAuto_ConnectDisconnectRunActionCall("192.168.0.5",0,tmpWaitTime)
    SimTestAuto_ConnectDisconnectRunActionCall("192.168.0.6",0,tmpWaitTime)
    SimTestAuto_ConnectDisconnectRunActionCall("192.168.0.2",0,tmpWaitTime)
    MessageBox("Info","Simulated Run1 Ended")
    return None

def TestStub_actionDebugTest2Handler():

    ClientDisConnectedGUIRefresh(EditBoxSearch1.text().strip())
    return None

def TestStub_actionDebugTest1Handler():
    SimTestAuto_ConnectDisconnectRun()
    return None

    ClientConnectedGUIRefresh(EditBoxSearch1.text().strip())
    return None

    global ui
    #KALINANNN MsgBox    
    #AppDebugMan.DebugInfo(EditBoxSearch1.text())
    #MessageBox("Bilgi",EditBoxSearch1.text())
    allRows = ui.tableWidget1.rowCount()
    for row in range(0,allRows):
        twi0 = ui.tableWidget1.item(row,0)
        twi1 = ui.tableWidget1.item(row,1)
        twi2 = ui.tableWidget1.item(row,2)
        #twi1 = ui.tableWidget1.cellWidget(row,1)
        #twi2 = ui.tableWidget1.cellWidget(row,2)
        AppDebugMan.DebugInfo("IP="+twi2.text())
    #for i in range (ui.tableWidget1.rowCount()):
    #AppDebugMan.DebugInfo(ui.tableWidget1.item[i][2])
    
    return None
#actionDebugTest1Handler() ENDs..

def TestThread1():
    global ui
    Thread1LocalCounter1=0
    while True:
        Thread1LocalCounter1+=1
        ui.textEditDebug1.setText(str(Thread1LocalCounter1))
        #AppDebugMan.DebugInfo("T1.LC1="+str(Thread1LocalCounter1))
    return None

#---------------------------------------------------------------
# TEST STUB CODE RANGE ENDs..
#---------------------------------------------------------------
#TODO=Framework library ye taşınacak. Non-Blocikng denenecek.
def MessageBox(prmStrTitle, prmStrMessage):
   msg = QMessageBox()
   msg.setIcon(QMessageBox.Information)

   msg.setText(prmStrMessage)
   #msg.setInformativeText("This is additional information")
   msg.setWindowTitle(prmStrTitle)
   #msg.setDetailedText("The details are as follows:")
   #msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
   msg.setStandardButtons(QMessageBox.Ok)
   msg.buttonClicked.connect(msgbtn)
	
   retval = msg.exec_()
   #print ("value of pressed message box button:"+ str(retval))

def msgbtn(i):
   #print ("Button pressed is:"+ str(i))
   pass

def actionExitHandler():
    AppDebugMan.DebugInfo("User wanted to exit")
    AppDebugMan.DebugClose()
    sys.exit(0)
    return None

def AddStyleSheetsToCombo():
    global ComboBoxStyleSheets
    ComboBoxStyleSheets.addItem("<< Theme Select  >>",1)
    ComboBoxStyleSheets.setPlaceholderText="<< Theme Select  >>"
    #TODO=strPath2StyleSheetsFolder ini file da yer alacak.
    strPath2StyleSheetsFolder="C:\\Users\\erhan\\OneDrive\\Masaüstü\\Erhan_2021.04.05\\PythonTry1\\StyleSheets"

    for f in os.listdir(strPath2StyleSheetsFolder):
        if os.path.isfile(strPath2StyleSheetsFolder+"\\"+f):
            if f.endswith(".qss"):
                ComboBoxStyleSheets.addItem(os.path.splitext(f)[0])

    ComboBoxStyleSheets.setCurrentIndex(-1)
    return None
#AddStyleSheetsToCombo ENDs..

def ComboBoxStyleSheets_SelectedItemChanged():
    #print("SelectedItemText=["+ComboBoxStyleSheets.currentText()+"] Selected ITemIndex=["+str(ComboBoxStyleSheets.currentIndex())+"]")
    
    #PlaceholderText Item shouldn't be selected
    if ComboBoxStyleSheets.currentIndex()==0:
        ComboBoxStyleSheets.setCurrentIndex(-1)
        return None
    #TODO=strPath2StyleSheetsFolder ini file da yer alacak.
    strPath2StyleSheetsFolder="StyleSheets\\"
    fileStyle = open(strPath2StyleSheetsFolder+ComboBoxStyleSheets.currentText()+".qss",'r')

    with fileStyle:
	    qss = fileStyle.read()
	    AppMain.setStyleSheet(qss)
    return None
#ComboBoxStyleSheets_SelectedItemChanged ENDs

def AddNewRowToGrid(prmStrNodeId,prmStrNodeDesc,prmStrIPNo,prmStrLocationDesc,prmStrConnectionState,prmStrActivityDesc,prmStrRegistered):
    global ui
    rc=ui.tableWidget1.rowCount()
    ui.tableWidget1.insertRow(ui.tableWidget1.rowCount())
    #TODO=Kolon indeksleri yerine kolon adları şeklinde sabitler kullanılacak
    ui.tableWidget1.setItem(rc,0,QTableWidgetItem(prmStrNodeId))
    ui.tableWidget1.setItem(rc,1,QTableWidgetItem(prmStrNodeDesc))
    ui.tableWidget1.setItem(rc,2,QTableWidgetItem(prmStrIPNo))
    ui.tableWidget1.setItem(rc,3,QTableWidgetItem(prmStrLocationDesc))        
    ui.tableWidget1.setItem(rc,4,QTableWidgetItem(prmStrConnectionState))        
    ui.tableWidget1.setItem(rc,5,QTableWidgetItem(prmStrActivityDesc))        
    ui.tableWidget1.setItem(rc,6,QTableWidgetItem(prmStrRegistered))      
    #rc=ui.tableWidget1.rowCount()
    #ui.tableWidget1.insertRow(ui.tableWidget1.rowCount())
    #ui.tableWidget1.setItem(rc,0,QTableWidgetItem("DENEME-"+str(rc)))
    #ui.tableWidget1.setItem(rc,1,QTableWidgetItem("DENEME-"+str(rc)))
    #ui.tableWidget1.setItem(rc,2,QTableWidgetItem("DENEME-"+str(rc)))
    return None
def AddClientNodes2GridFromSettings():
    global ui
    AppDebugMan.DebugInfo(AppSpoManager.NodesList)
    stringLines=AppSpoManager.NodesList.split("\n")
    rows, cols = (10, 4)
    NodesArray =[[0 for i in range(cols)] for j in range(rows)]

    for i in range (len(stringLines)):
        #AppDebugMan.DebugInfo("Node["+str(i)+"]=["+stringTokens[i]+"]")
        NodesArray[i][0]=i
        stringTokensInLine=stringLines[i].split(",")
        NodesArray[i][1]=stringTokensInLine[0].strip()
        NodesArray[i][2]=stringTokensInLine[1].strip()
        NodesArray[i][3]=stringTokensInLine[2].strip()
        
   
    AppDebugMan.DebugInfo("List of All Nodes Read From IniFile------")
    for i in range (len(stringLines)):
        AppDebugMan.DebugInfo("Node["+str(i)+"] Order=["+str(NodesArray[i][0])+"] IP="+NodesArray[i][1]+"] Place=]"+NodesArray[i][2]+"] Desc=["+NodesArray[i][3]+"]")
        AddNewRowToGrid(str(NodesArray[i][0]),str(NodesArray[i][3]),str(NodesArray[i][1]),str(NodesArray[i][2]),"NOT Connected","N/A","Yes")
        #TODO=string ifadeler sabitler olarak tanımlanacak.

    
    return None



#Gridde bulunmayan, yani ini file dan okunmamış ve ayrıca o ana kadar gelmemiş (bağlanmamış) bir Client Node ilk kez bağlandığında çağırılır.
#Bu tür client lar Ghost olarak adlandırılır
def AddNewGhostClientToGrid(prmStrIPNo):
    AddNewRowToGrid("Unknown ID","Unknown Description",prmStrIPNo,"Not Known","Connected","None","NO")
    #TODO=Stringler sabit haline getirilecek.
    return None

def UpdateGridRowForNewDisConnectedClient(prmRowIndx):
    global ui
    
    ui.tableWidget1.item(prmRowIndx,4).setText("DISCONNECTED NEWLY") 
    #TODO=Vx de blink yapılacak.
    
    return None

def UpdateGridRowForNewConnectedClient(prmRowIndx):
    global ui
    
    ui.tableWidget1.item(prmRowIndx,4).setText("CONNECTED NEWLY") 
    #TODO=Vx de blink yapılacak.
    
    return None

def FindClientIPInGrid(prmStrIPNo):
    global ui
    #KALINANNN MsgBox    
    #AppDebugMan.DebugInfo(EditBoxSearch1.text())
    #MessageBox("Bilgi",EditBoxSearch1.text())
    allRows = ui.tableWidget1.rowCount()
    for indxrow in range(0,allRows):
        strNodeId = ui.tableWidget1.item(indxrow,0).text()
        strNodeDesc= ui.tableWidget1.item(indxrow,1).text()
        strNodeIp = ui.tableWidget1.item(indxrow,2).text()
        #twi1 = ui.tableWidget1.cellWidget(row,1)
        #twi2 = ui.tableWidget1.cellWidget(row,2)
        #AppDebugMan.DebugInfo("IP="+twi2.text())
        if strNodeIp == prmStrIPNo:
            return indxrow

    return -1 #TODO=Notfound constant tanımlanacak

#Belirli bir IP ile bağlantı kesildiğinde veya HeartBeat alınamadığında durumun grid satırında günceller
#Belirli bir IP ile bağlantı kopmuş ise bu IP li client kaydının gridde mutlaka bulunuyor olması gerekir.
#Bulunmaması durumu asla oluşmaması gereken bir durumdur. Gereken yapılır.
#Ayrıca gridde bulunuyor ise de bağlantı durumunun o anda mevcutda Connected olması gerekir. 
#Eğer değil ise bu da asla oluşmaması gereken bir durumdur. Gereken yapılır.
def ClientDisConnectedGUIRefresh(prmStrIPNo):
    indxFound=FindClientIPInGrid(prmStrIPNo)
    if indxFound==-1:
        AppDebugMan.DebugInfo("Bağlantısı Kopan IP=["+prmStrIPNo+"] Gridde bulunamadı. ERR_030421_2353")
    else:
        AppDebugMan.DebugInfo("Gridde ["+str(indxFound)+"]. satırda bulunan Client ile Bağlantı Koptu")
        #TODO=Gridde bulunuyor ama o anki bağlantı durumu Connected değil ise olmaması gereken durumu handle
        UpdateGridRowForNewDisConnectedClient(indxFound)
        
    return None

#Her türlü durumda (girdde olsun olmasın, inifile dan okunsun okunmasın) yeni gelen bir client bağlantısı durumunda çağrılır.
def ClientConnectedGUIRefresh(prmStrIPNo):
    indxFound=FindClientIPInGrid(prmStrIPNo)
    if indxFound==-1:
        AppDebugMan.DebugInfo("Gridde bulunmayan bir Client Node Bağlandı")
        #Gridde bulunmayan, yani ini file dan okunmamış ve ayrıca o ana kadar gelmemiş (bağlanmamış) bir Client Node ilk kez bağlandı.
        #bu durumda yapılacak işlemler başlatılır. Bu tür client lar Ghost olarak adlandırılır
        AddNewGhostClientToGrid(prmStrIPNo)
    else:
        AppDebugMan.DebugInfo("Gridde ["+str(indxFound)+"]. satırda bulunan bir Client Node Bağlandı")
        #Gridde zaten bulunan (ya ini file dan okunmuş ya da okunmadığı halde önceden gelmiş (bağlanmış) bir Client Node bağlantı kurdu.
        #bu durumda yapılacak işlemler başlatılır.
        UpdateGridRowForNewConnectedClient(indxFound)
        
    return None
#-------------------------------------------------------
# MAIN STARTs
#-------------------------------------------------------

#Create Application Global Command Line Parser Object
AppCliManager=CliParser()

#Create Application Global Settings&Parameters&Options (SPO) Manager Object
AppSpoManager=SpoManager(AppCliManager.inifilename,os.path.dirname(__file__),AppCliManager.DebugVerboseMode)

#Prepare application main window
AppMain = QtWidgets.QApplication([])
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

#Create & Prepare StyleSheets Selection Combo
ComboBoxStyleSheets = QtWidgets.QComboBox()
ui.toolBar.addWidget(ComboBoxStyleSheets)
AddStyleSheetsToCombo()
ComboBoxStyleSheets.activated.connect(ComboBoxStyleSheets_SelectedItemChanged)

#Create & Prepare Search EditBox
EditBoxSearch1 = QtWidgets.QLineEdit()
ui.toolBar.addSeparator()
ui.toolBar.addSeparator()
ui.toolBar.addWidget(EditBoxSearch1)
EditBoxSearch1.setMaximumWidth(300)
EditBoxSearch1.setText("192.168.0.4")


#Create Application Global Debug Manager Object
AppDebugMan=DebugManager(AppSpoManager,ui.tabWidget,1,ui.textEditDebug1)

AppDebugMan.DebugInfo("Main Program Started")

AppDebugMan.DebugInfo("Command Line iniFileName="+AppSpoManager.inifilename)
AppDebugMan.DebugInfo("Command Line VerboseMode="+str(AppCliManager.DebugVerboseMode))

#dump all application wide settings, parameters, options
AppDebugMan.DebugInfo("AppSpoManager.DebugVerboseModeOn="+str(AppSpoManager.DebugVerboseModeOn))
AppDebugMan.DebugInfo("AppSpoManager.AppDebugMan.DebugInfoMessages="+str(AppSpoManager.DebugInfoMessages))
AppDebugMan.DebugInfo("AppSpoManager.DebugErrorMessages="+str(AppSpoManager.DebugErrorMessages))
AppDebugMan.DebugInfo("AppSpoManager.DebugTargetConsole="+str(AppSpoManager.DebugTargetConsole))
AppDebugMan.DebugInfo("AppSpoManager.DebugTargetFile="+str(AppSpoManager.DebugTargetFile))
AppDebugMan.DebugInfo("AppSpoManager.DebugTargetFilePath="+AppSpoManager.DebugTargetFilePath)
AppDebugMan.DebugInfo("AppSpoManager.DebugLinesPerFile="+str(AppSpoManager.DebugLinesPerFile))
AppDebugMan.DebugInfo("AppSpoManager.AppRunFolder="+AppSpoManager.AppRunFolder)
#TODO=Dynamic olarak AppSpoManager tüm itemları yazdırılacak

strPath = __file__
listPath = strPath.split(os.sep)
strModuleFileName=listPath[len(listPath)-1]
AppDebugMan.DebugInfo("ModuleFileNameOnly="+strModuleFileName)

AppDebugMan.DebugInfo("File="+__file__)
AppDebugMan.DebugInfo("FileDirName="+os.path.dirname(__file__))
AppDebugMan.DebugInfo("FileAbsPath="+os.path.abspath(__file__))
AppDebugMan.DebugInfo("ModuleName1="+__name__)
AppDebugMan.DebugInfo("ModuleName2="+inspect.getmodulename(__file__))

AppDebugMan.DebugInfo("Main Program Started")
AppDebugMan.DebugInfo("Python Executable Path="+sys.executable)
AppDebugMan.DebugInfo("Python Interpreter Version="+sys.version)
AppDebugMan.DebugInfo("PythonShellProcessPID="+str(os.getpid()))
AppDebugMan.DebugInfo("PythonShellParentProcessPID="+str(os.getppid()))

strTemp="Sys.Path=%s" % (sys.path)
AppDebugMan.DebugInfo(strTemp)


#Show application main window
MainWindow.showMaximized()


#Attach event handlers
ui.pushButtonAddRow.clicked.connect(TestStub_buttonAddRowClick)
ui.pushButton_2.clicked.connect(TestStub_button2Click)
ui.actionDebugTest1.triggered.connect(TestStub_actionDebugTest1Handler)
ui.actionDebugTest2.triggered.connect(TestStub_actionDebugTest2Handler)
ui.actionExit.triggered.connect(actionExitHandler)


AddClientNodes2GridFromSettings()


#NP=CREATE_OTHER_THREADs STARTs...
Thread2_1=TestThread2("TH1")
Thread2_1.UpdaterSignal.connect(on_data_ready)
Thread2_1.start()

Thread2_2=TestThread2("TH2")
Thread2_2.UpdaterSignal.connect(on_data_ready)
Thread2_2.start()



AppDebugMan.DebugInfo("Creating TestThread1")
#Thread1= threading.Thread(target=TestThread1)
AppDebugMan.DebugInfo("Created TestThread1")

AppDebugMan.DebugInfo("Starting TestThread1")
#Thread1.start()
AppDebugMan.DebugInfo("Started TestThread1")
#NP=CREATE_OTHER_THREADs ENDs...
AppDebugMan.DebugInfo("Showing MainWindow")
sys.exit(AppMain.exec_())
AppDebugMan.DebugInfo("Showed MainWindow")
AppDebugMan.DebugInfo("Main Exit Never Printed")
#DebugClose() #Debug file close un GUI kapanırken mutlaka çalışması sağlanacak..GUI olmasa da kapanmalı..

#-------------------------------------------------------
# MAIN ENDs
#-------------------------------------------------------


