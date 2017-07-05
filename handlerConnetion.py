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
from Battery import Battery
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


def start_delivery(arg):
    print '\n'
    print "VAMOOOOOOOOOOOOOOOOOOOOOOOO"
    print '\n'
    #Identificadores de caminho
        # Secretaria-Biblioteca
        # --
        #Biblioteca-UED
        # --
        #
    # Comando para Ligar o robô
    # GPIO.output(21)
    # time.sleep(0.5)
    # ser.write(identificadorDeCaminho)

def main():

    sendSMS = SendSMS()
    battery = Battery(ws)
    delivery = Delivery(ws)
    result = ws.recv()
    result = json.loads(result)
    pprint("RESULTADO %s"  %result)

    # nivelBateria = GPIO.input(12)
    nivelBateria = "Medio"
    # result

    if result.get('type') == None:

        show = result.get('message')
        pprint(show)

        if show.get('type') == "Delivery":
            destination = show.get('destination').get('departament_name')
            print destination
            # Capturar a rota de envio e direcionar para o carrinho
            pprint(show.get('route'))

            sender_name = show.get('sender').get('employee_name')
            sender_number = show.get('sender').get('contacts')[0].get('description')

            recipient_name = show.get('recipient').get('employee_name')
            recipient_number = show.get('recipient').get('contacts')[0].get('description')
            sendSMS.smsForSender(recipient_name, recipient_number, destination)

            #Identificadores de caminho
                # Secretaria-Biblioteca
                # --
                #Biblioteca-UED
                # --
                #
            #start_delivery("Secretaria-Biblioteca");

        if show.get('type') == "Open":
            pass
        if show.get('type') == "infoAdmin":
            pprint(show.get('admins'))
            admin_name = show.get('admins')[0].get('name')
            admin_contact = show.get('admins')[0].get('contact')
            sendSMS.informStatusBatterry(admin_name, admin_contact)

    if nivelBateria == "Baixo":
        pass
    if nivelBateria == "Medio":
        battery.get_admins("MESSAGE")
    if nivelBateria == "Alto":
        pass

    # resposta = ser.readline()
    # balanca = GPIO.input(10)
    #
    # if (resposta == "Aviso") :
    #     aviso = ser.readline() #INICIO, FIM, OBSTRUIDO
    # if (resposta == "Deslocamento") :
    #     deslocamento = ser.readline() #NUMERO DE VEZES QUE DESLOCOU NO EIXO X.
    # time.sleep(0.5)


if __name__ == "__main__":
    while 1:
        main()



# ws.send(json.dumps('{"identifier":"{"channel":"RoomChannel"},"command":"speak()"}'))


# # ws.recv(r'{"identifier":"message","type":"message"}')
# ws.send (r'[{"identifier"=>{"channel"=>"RoomChannel"}, "command"=> "subscribe"}]')

 # for x in range(10):
 #     ws.send(r'[{identifier:{channel: "RoomChannel"}, "command": subscribe}]')
