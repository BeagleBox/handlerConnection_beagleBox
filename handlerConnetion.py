# No caso eu to mandando uma mensagem "aviso" e "Desolocamento"
# pra identificar o tipo de dado que eu estou enviando,
# a questão do nivel de bateria, e da balança a agente vai pegar da propria placa,
# ou seja, vai tá disponível a todo momento, não vai vir do arduino

import json
import pprint
import sys
from SendSMS import SendSMS
from Delivery import Delivery
from websocket import create_connection
import RPi.GPIO as GPIO
import time
import serial

#Configura a serial e a velocidade de transmissao
ser = serial.Serial("/dev/ttyAMA0", 115200)
GPIO.setmode(GPIO.BOARD)
#Entrada do sinal da balança
GPIO.setup(10,GPIO,IN)
#Entrada do sinal do nivel de bateria
GPIO.setup(12,GPIO,IN)

ser.write(identificadorDeCaminho)



ws = create_connection("ws://localhost:3000/cable")

def main():
    delivery = Delivery(ws)
    result = ws.recv()
    result = json.loads(result)
    print result
    print result.get("type")

    balanca = GPIO.input(10)
    nivelBateria = GPIO.input(12)
    resposta = ser.readline()
        if (resposta == "Aviso") :
                aviso = ser.readline() #INICIO, FIM, OBSTRUIDO
        if (resposta == "Deslocamento") :
                deslocamento = ser.readline() #NUMERO DE VEZES QUE DESLOCOU NO EIXO X.
        if (trancar == 1) :
                ser.write(trancar)

        time.sleep(0.5)


if __name__ == "__main__":
    while 1:
        main()



# ws.send(json.dumps('{"identifier":"{"channel":"RoomChannel"},"command":"speak()"}'))


# # ws.recv(r'{"identifier":"message","type":"message"}')
# ws.send (r'[{"identifier"=>{"channel"=>"RoomChannel"}, "command"=> "subscribe"}]')

 # for x in range(10):
 #     ws.send(r'[{identifier:{channel: "RoomChannel"}, "command": subscribe}]')
