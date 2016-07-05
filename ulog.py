import sys

L_DEBUG    = 0
L_INFO     = 1
L_WARNING  = 2
L_ERROR    = 3
L_CRITICAL = 4

class ULog(object):
    def __init__(self):
        self.name = ""
        self.debug_prefix    = "DEBUG"
        self.info_prefix     = "INFO"
        self.warning_prefix  = "WARNING"
        self.error_prefix    = "ERROR"
        self.critical_prefix = "CRITICAL"
        self.level = 0
        self.outputs = [sys.stdout,]
        self.messages = []
        self.normal = "\033[0m"
        self.red = "\033[31m"
        self.bold = "\033[1m"
        self.blink = "\033[5m"
        self.underlined = "\033[4m"
        self.lightgreen = "\033[92m"

    def set_name(self, name):
        self.name = name

    def set_level(self, level):
        self.level = (level if (level>0 and level<=3) else 0)

    def debug(self, message):
        if self.level == 0:
            message = self.name+"::"+self.debug_prefix+"::"+message+'\r\n'
            for o in self.outputs:
                o.write(message)
            self.messages.append(message)

    def info(self, message):
        if self.level <= 1:
            message = self.lightgreen+self.name+"::"+self.info_prefix+"::"+message+self.normal+'\r\n'
            for o in self.outputs:
                o.write(message)
            self.messages.append(message)

    def warn(self, message):
        if self.level <= 1:
            message = self.underlined+self.name+"::"+self.warning_prefix+"::"+message+self.normal+'\r\n'
            for o in self.outputs:
                o.write(message)
            self.messages.append(message)

    def error(self, message):
        if self.level <= 1:
            message = self.red+self.name+"::"+self.error_prefix+"::"+message+self.normal+'\r\n'
            for o in self.outputs:
                o.write(message)
            self.messages.append(message)

    def critical(self, message):
        if self.level <= 1:
            message = self.red+self.bold+self.name+"::"+self.critical_prefix+"::"+message+self.normal+'\r\n'
            for o in self.outputs:
                o.write(message)
            self.messages.append(message)


ulog = ULog()
