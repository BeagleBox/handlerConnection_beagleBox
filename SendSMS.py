from twilio.rest import Client

# class SendSMS(object):
#     """docstring for SendSMS."""
#     def __init__(self):
#         super(SendSMS, self).__init__()
#         self.account = "AC8041f486b04273feea9a0a9f67058ba9"
#         # self.token = "d98e829de9545b0c81ebf4753b00b49c"
#         # self.client = Client(self.account, self.token)
#
#         def check(self,):
#             print self.account
#         #
#         # def sender_sms(self):
#         #
class SendSMS(object):
    """docstring for Delivery."""
    def __init__(self):
        super(SendSMS, self).__init__()
        self.account = "AC233449a7d51e4c884ca79ee9f094c218"
        self.token = "cfc5d149a8260a204d9a98acc930aeb6"
        self.client = Client(self.account, self.token)

    def smsForSender(self,name,contact, destination,id,senha):
        contact= "+%s" %contact
        body = ("%s vc recebeu uma entrega destinada para %s,com ID %s SENHA %s" %(name,destination,id,senha))
        message = self.client.messages.create(to=contact,from_="+14243584090",body=body)


    def informStatusBatterry(self,name,contact):
        contact= "+%s" %contact
        body = ("%s atencao ao status da bateria: MEDIO " %(name))
        message = self.client.messages.create(to=contact,from_="+14243584090",body=body)


    def stop_delivery(self,argument):
        print argument
        message = r'{"command":"message","identifier":"{\"channel\":\"DeliveryChannel\"}","data":"{\"message\":\"%s\",\"action\":\"stop_delivery\"}"}' %(argument)
        # self.ws.send(message)

    def open_car(arg):
        pass

    def lock_car(arg):
        pass
