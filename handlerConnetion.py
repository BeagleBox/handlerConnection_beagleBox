import json
import pprint
from Delivery import Delivery
from websocket import create_connection
ws = create_connection("ws://localhost:3000/cable")


delivery = Delivery(ws)


result = ws.recv()
print result

delivery.start_delivery("esddd")
print "------"
result = ws.recv()
print result


ws.close




# ws.send(json.dumps('{"identifier":"{"channel":"RoomChannel"},"command":"speak()"}'))


# # ws.recv(r'{"identifier":"message","type":"message"}')
# ws.send (r'[{"identifier"=>{"channel"=>"RoomChannel"}, "command"=> "subscribe"}]')

 # for x in range(10):
 #     ws.send(r'[{identifier:{channel: "RoomChannel"}, "command": subscribe}]')
