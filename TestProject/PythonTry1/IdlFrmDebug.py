import inspect
import os
from datetime import datetime

class DebugManager:
  def __init__(self,prmSPOManager,prmDebugtabWidget,prmDebugtabWidgetTabIndex,prmtextEditDebug1):
    self.DebugSourceNodeID=prmSPOManager.NodeId
    self.IsDebugVerboseMode=prmSPOManager.DebugVerboseModeOn
    self.DebugTargetConsole=prmSPOManager.DebugTargetConsole
    self.DebugInfoMessages=prmSPOManager.DebugInfoMessages
    self.DebugErrorMessages=prmSPOManager.DebugErrorMessages
    self.DebugTargetFile=prmSPOManager.DebugTargetFile
    self.AppRunFolder=prmSPOManager.AppRunFolder
    self.DebugTargetFilePath=prmSPOManager.DebugTargetFilePath
    self.DebugLinesPerFile=prmSPOManager.DebugLinesPerFile
    self.DebugFieldsTimestamp=prmSPOManager.DebugFieldsTimestamp
    self.DebugLinesWrittenAll=0
    self.DebugNofFilesCreated=0
    self.DebugShowOnGUI=prmSPOManager.DebugShowOnGUI
    self.DebugShowOnGUIPassword=prmSPOManager.DebugShowOnGUIPassword
    self.DebugtabWidget=prmDebugtabWidget
    self.DebugtabWidgetTabIndex=prmDebugtabWidgetTabIndex
    self.DebugtextEdit1=prmtextEditDebug1
    self.ActiveDebugFileNameFull=""
    self.DebugFileNameFixedSessionStr=datetime.now().strftime("%Y.%m.%d.%H.%M.%S.%f")
    self.DebugNofFilesCreated=0
    self.DebugFileHandler=None
    self.DebugLinesWrittenToFile=0
    self.ActiveDebugFileTimestamp=""
    self.ActiveDebugLineStr=""

    if self.DebugTargetFile:
      self.OpenDebugFile()

    if self.DebugShowOnGUI==True and self.DebugShowOnGUIPassword == "112233445566": #TODO=Dahili GUI ye debug açma şifresi gizli sabitlere taşınacak.
      self.DebugShowOnGUIAuthanticated=True
    else:
      self.DebugtabWidget.removeTab(self.DebugtabWidgetTabIndex)
      self.DebugShowOnGUIAuthanticated=False

    return  None
    #__init__(self,prmSPOManager): ENDs...




  def OpenDebugFile(self):
    
    self.DebugNofFilesCreated+=1
    #TODO=File name pattern ve sabitler 
    self.ActiveDebugFileNameFull=self.AppRunFolder+"\\"+self.DebugTargetFilePath+"\\Debug"+self.DebugFileNameFixedSessionStr+"_"+str(self.DebugNofFilesCreated)+".txt"
    self.DebugFileHandler = open(self.ActiveDebugFileNameFull, "a")
    self.DebugLinesWrittenToFile=0

  
  def DebugCommonOps(self,prmstrTypePrefix,strMsg):
    (frame,filename,line_number,function_name, lines, index) = inspect.getouterframes(inspect.currentframe())[2]
    listPath = filename.split(os.sep)
  
    self.DebugLinesWrittenAll+=1
    if self.DebugFieldsTimestamp:
      self.ActiveDebugFileTimestamp=datetime.now().strftime("[%Y.%m.%d.%H.%M.%S.%f].")
    else:
      self.ActiveDebugFileTimestamp=""
    
    self.ActiveDebugLineStr="[%04d].[%d].[%d].%s%s.%s:%s.%s.%s:%s" % (self.DebugLinesWrittenAll,os.getppid(),os.getpid(),self.ActiveDebugFileTimestamp,
          str(self.DebugSourceNodeID),prmstrTypePrefix,listPath[len(listPath)-1],function_name, line_number,strMsg)
    
		
    if self.DebugTargetConsole:
      print(self.ActiveDebugLineStr,sep='') #TODO=sep değeri sabitlere eklenecek
    if self.DebugShowOnGUIAuthanticated:
      self.DebugtextEdit1.append(self.ActiveDebugLineStr)
    
    if self.DebugTargetFile:
      self.DebugFileHandler.write(self.ActiveDebugLineStr+"\n") #TODO=EOL karfakteri sabitlere eklenecek
      self.DebugLinesWrittenToFile+=1
      if self.DebugLinesWrittenToFile==self.DebugLinesPerFile:
        self.DebugFileHandler.close()
        self.OpenDebugFile()

  def DebugInfo(self,strMsg):
    if ((not self.IsDebugVerboseMode) or (not self.DebugInfoMessages)):
      return
    self.DebugCommonOps("INF",strMsg) #TODO=Information Prefix INF sabitlere eklenecek


  def DebugErr(self,strMsg):
    if ((not self.IsDebugVerboseMode) or (not self.DebugErrorMessages)):
      return
    self.DebugCommonOps("ERR",strMsg) #TODO=Error Prefix ERR sabitlere eklenecek

  def DebugClose(self,):
    if self.DebugTargetFile:
      self.DebugFileHandler.close()

if __name__ == "__main__":
    print("CAN NOT BE RUN DIRECTLY")