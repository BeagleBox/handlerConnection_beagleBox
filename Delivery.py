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

    def stop_delivery(arg):
        pass

    def open_car(arg):
        pass

    def lock_car(arg):
        pass
