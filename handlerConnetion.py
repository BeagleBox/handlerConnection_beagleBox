import json
import pprint
from websocket import create_connection
ws = create_connection("ws://localhost:3000/cable")
ws.send(r'{"command":"subscribe","identifier":"{\"channel\":\"DeliveryChannel\"}"}')
result = ws.recv()


print result



ws.send( r'{"command":"message","identifier":"{\"channel\":\"DeliveryChannel\"}","data":"{\"message\":\"hello from user2\",\"action\":\"start_delivery\"}"}')


# ws.send(json.dumps('{"identifier":"{"channel":"RoomChannel"},"command":"speak()"}'))


# # ws.recv(r'{"identifier":"message","type":"message"}')
# ws.send (r'[{"identifier"=>{"channel"=>"RoomChannel"}, "command"=> "subscribe"}]')

 # for x in range(10):
 #     ws.send(r'[{identifier:{channel: "RoomChannel"}, "command": subscribe}]')
