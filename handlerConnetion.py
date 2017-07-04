#!/usr/bin/env python
# -*- coding: utf-8 -*-
# No caso eu to mandando uma mensagem "aviso" e "Desolocamento"
# pra identificar o tipo de dado que eu estou enviando,
# a questão do nivel de bateria, e da balança a agente vai pegar da propria placa,
# ou seja, vai tá disponível a todo momento, não vai vir do arduino
class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

from SendSMS import SendSMS
import json
from pprint import pprint
import sys
from Delivery import Delivery
from websocket import create_connection
from collections import OrderedDict
# import RPi.GPIO as GPIO
# import serial
import time

# #Configura a serial e a velocidade de transmissao
# ser = serial.Serial("/dev/ttyAMA0", 115200)
# GPIO.setmode(GPIO.BOARD)
# #Entrada do sinal da balança
# GPIO.setup(10,GPIO,IN)
# #Entrada do sinal do nivel de bateria
# GPIO.setup(12,GPIO,IN)
# ser.write(identificadorDeCaminho)



ws = create_connection("ws://localhost:3000/cable")


def serialize_instance(obj):
    d = { '__classname__' : type(obj).__name__ }
    d.update(vars(obj))
    return d

def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)   # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
            return obj
    else:
        return d

def main():

    sendSMS = SendSMS()
    delivery = Delivery(ws)
    result = ws.recv()
    result = json.loads(result)
    # pprint(result)

    # result

    if result.get('type') == None:
        show = result.get('message')
        destination = show.get('destination').get('departament_name')
        print destination

        if show.get('type') == "Delivery":

            # Capturar a rota de envio e direcionar para o carrinho
            pprint(show.get('route'))

            sender_name = show.get('sender').get('employee_name')
            sender_number = show.get('sender').get('contacts')[0].get('description')
            sendSMS.smsForSender(sender_name, sender_number, destination)

            recipient = show.get('recipient').get('contacts')[0].get('description')


            print sender_name
            print recipient




        if show.get('type') == "Lock":
            pass


    # nivelBateria = GPIO.input(12)
    # resposta = ser.readline()
    # balanca = GPIO.input(10)
    #
    # if (resposta == "Aviso") :
    #     aviso = ser.readline() #INICIO, FIM, OBSTRUIDO
    # if (resposta == "Deslocamento") :
    #     deslocamento = ser.readline() #NUMERO DE VEZES QUE DESLOCOU NO EIXO X.
    time.sleep(0.5)


if __name__ == "__main__":
    while 1:
        main()



# ws.send(json.dumps('{"identifier":"{"channel":"RoomChannel"},"command":"speak()"}'))


# # ws.recv(r'{"identifier":"message","type":"message"}')
# ws.send (r'[{"identifier"=>{"channel"=>"RoomChannel"}, "command"=> "subscribe"}]')

 # for x in range(10):
 #     ws.send(r'[{identifier:{channel: "RoomChannel"}, "command": subscribe}]')
