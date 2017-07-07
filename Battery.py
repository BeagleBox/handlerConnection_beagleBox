class Battery(object):
    """docstring for Battery."""
    def __init__(self, arg):
        super(Battery, self).__init__()
        self.arg = arg
        self.ws = arg
        self.ws.send(r'{"command":"subscribe","identifier":"{\"channel\":\"BatteryChannel\"}"}')

    def inform(self,argument):
        message = r'{"command":"message","identifier":"{\"channel\":\"BatteryChannel\"}","data":"{\"message\":\"%s\",\"action\":\"inform\"}"}' %(argument)
        self.ws.send(message)

    def get_admins(self,argument):
        message = r'{"command":"message","identifier":"{\"channel\":\"BatteryChannel\"}","data":"{\"message\":\"%s\",\"action\":\"getAdmins\"}"}' %(argument)
        self.ws.send(message)

    def change(self,argument):
        message = r'{"command":"message","identifier":"{\"channel\":\"BatteryChannel\"}","data":"{\"message\":\"%s\",\"action\":\"changestatus\"}"}' %(argument)
        self.ws.send(message)
