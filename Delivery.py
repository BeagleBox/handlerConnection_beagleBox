class Delivery(object):
    """docstring for Delivery."""
    def __init__(self, arg):
        super(Delivery, self).__init__()
        self.arg = arg
        self.ws = arg
        self.ws.send(r'{"command":"subscribe","identifier":"{\"channel\":\"DeliveryChannel\"}"}')

    def start_delivery(self,argument):
        print argument
        message = r'{"command":"message","identifier":"{\"channel\":\"DeliveryChannel\"}","data":"{\"message\":\"%s\",\"action\":\"start_delivery\"}"}' %(argument)
        self.ws.send(message)

    def stop_delivery(self,argument):
        print argument
        message = r'{"command":"message","identifier":"{\"channel\":\"DeliveryChannel\"}","data":"{\"message\":\"%s\",\"action\":\"stop_delivery\"}"}' %(argument)
        self.ws.send(message)

    def update_delivery(self,argument,tracker):
        message = r'{"command":"message","identifier":"{\"channel\":\"DeliveryChannel\"}","data":"{\"message\":\"%s\",\"tracker\":\"%s\",\"action\":\"update_delivery\"}"}' %(argument, tracker)
        self.ws.send(message)

    def update_status(self,argument,tracker):
        message = r'{"command":"message","identifier":"{\"channel\":\"DeliveryChannel\"}","data":"{\"message\":\"%s\",\"tracker\":\"%s\",\"action\":\"update_status\"}"}' %(argument, tracker)
        self.ws.send(message)

    def open_car(arg):
        pass

    def lock_car(arg):
        pass
