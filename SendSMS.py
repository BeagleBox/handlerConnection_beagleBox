from twilio.rest import Client

class SendSMS(object):
    """docstring for SendSMS."""
    def __init__(self, arg):
        super(SendSMS, self).__init__()
        self.account = "AC8041f486b04273feea9a0a9f67058ba9"
        self.token = "d98e829de9545b0c81ebf4753b00b49c"
        self.client = Client(account, token)

        def sendTeste(self):
            message = self.client.messages.create(to="+5561991793268",from_="+17088882236",body="Hello there!")
