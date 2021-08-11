#Command Line Inteface Parameters&options Parser Class
from configparser import ConfigParser, NoOptionError, NoSectionError
import argparse

class CliParser:
    def __init__(self):
        
        argp = argparse.ArgumentParser()

        argp.add_argument ("-i", "--inifile",help="settings file to be used", dest='arginifilename', type=str)
        argp.add_argument("-v","--verbose", help="increase output verbosity",action="store_true",default=None)

        args = argp.parse_args()
        
        if args.arginifilename is None:
            self.inifilename="default.ini"
        else:
            self.inifilename=args.arginifilename

        self.DebugVerboseMode=args.verbose
        return None


if __name__ == "__main__":
    print("CAN NOT BE RUN DIRECTLY")