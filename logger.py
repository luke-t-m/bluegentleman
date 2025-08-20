from datetime import datetime
import sys

class Logger():
    def __init__(self):
        self.unsilence()
        self.settag()
        self.tag_map = dict()

    def silence(self):
        self.silent = True
    
    def unsilence(self):
        self.silent = False

    def settag(self, tag=""):
        self.tag = tag.upper().center(6)

    def log(self, msg, bold, colour, caller):
        if not self.silent:
            if caller in self.tag_map:
                self.tag = self.tag_map[caller]
            else:
                self.tag_map[caller] = self.tag
            timestamp = datetime.now().strftime("%H:%M:%S:%f")[:-1]
            print(f"[{timestamp}] [{self.tag}] {msg}")


logger = Logger()

def log(msg, bold=False, colour=None):
    caller = sys._getframe().f_back.f_code.co_name
    logger.log(msg, bold, colour, caller)

def logtag(tag):
    logger.settag(tag)