from configparser import ConfigParser, NoOptionError, NoSectionError
from IdlFrmDebug import *

class SpoManager:
    def __init__(self,strIniFileName,strAppRunFolder,boolDebugVerboseMode):
        
        self.inifilename=strIniFileName

        self.configParser = ConfigParser()
        self.configParser.read(self.inifilename)

        try:
            #Get all SPOs STARTs-----------------------------------
            self.DebugVerboseModeOn=self.configParser.getboolean('DEBUG','VerboseMode') #TODO=Sabitler ile ikinci kademe generic çalışma yapılacak.
            if boolDebugVerboseMode is not None:
                self.DebugVerboseModeOn=boolDebugVerboseMode

            self.DebugShowOnGUI=self.configParser.getboolean('DEBUG','DebugShowOnGUI')
            self.DebugShowOnGUIPassword=self.configParser.get('DEBUG','DebugShowOnGUIPassword')
            self.DebugShowOnGUIAuthanticated=False
            self.DebugInfoMessages=self.configParser.getboolean('DEBUG','DebugInfoMessages')
            self.DebugErrorMessages=self.configParser.getboolean('DEBUG','DebugErrorMessages')
            self.DebugTargetConsole=self.configParser.getboolean('DEBUG','DebugTargetConsole')
            self.DebugTargetFile=self.configParser.getboolean('DEBUG','DebugTargetFile')
            self.DebugTargetFilePath=self.configParser.get('DEBUG','DebugTargetFilePath')
            self.DebugLinesPerFile=self.configParser.getint('DEBUG','DebugLinesPerFile')
            self.DebugFieldsTimestamp=self.configParser.getboolean('DEBUG','DebugFieldsTimestamp')
            self.NodeId=self.configParser.get('APPLICATION','NodeId')
            self.NodesList=self.configParser.get('NODES','NodesList')
            self.AppRunFolder=strAppRunFolder
            
            #Get all SPOs ENDs-----------------------------------
            
        except NoOptionError as errNoOption:
            #DebugErr("Missing option name in the inifile (%s). Section=%s OptionName=%s " % (self.inifilename, errNoOption.section,errNoOption.option))
            print("Missing option name in the inifile (%s). Section=%s OptionName=%s " % (self.inifilename, errNoOption.section,errNoOption.option))
        except NoSectionError as errNoSection:
            #DebugErr("Missing section name in the inifile (%s). Section=%s" % (self.inifilename, errNoSection.section))
            print("Missing section name in the inifile (%s). Section=%s" % (self.inifilename, errNoSection.section))

if __name__ == "__main__":
    print("CAN NOT BE RUN DIRECTLY")