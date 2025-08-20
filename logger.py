from datetime import datetime
from collections import defaultdict
import sys

class Logger():
    def __init__(self):
        self.unsilence()
        self.tag_map = defaultdict(lambda: self.tag_format(""))

    def tag_format(tag):
        return tag.upper().center(6)

    def silence(self):
        self.silent = True
    
    def unsilence(self):
        self.silent = False

    def settag(self, tag, caller):
        self.tag_map[caller] = self.tag_format(tag)

    def log(self, msg, bold, colour, caller):
        if not self.silent:
            tag = self.tag_map[caller]
            timestamp = datetime.now().strftime("%H:%M:%S:%f")[:-1]
            print(f"[{timestamp}] [{tag}] {msg}")


logger = Logger()

def log(msg, bold=False, colour=None):
    caller = sys._getframe().f_back.f_code.co_name
    logger.log(msg, bold, colour, caller)

def logtag(tag):
    caller = sys._getframe().f_back.f_code.co_name
    logger.settag(tag, caller)