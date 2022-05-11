import time
from socket import *
serverName = '10.0.0.2'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
clientSocket.settimeout(1)

for i in range(1,11):

  try:
    message = 'Ping'+ str(i)
    startTime = time.time()
    clientSocket.sendto(message.encode(),(serverName,serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    returnTime = time.time()
    print('Mesg sent:', 'Ping'+ str(i))
    print('Mesg rcvd:', modifiedMessage.decode())
    print('Start time:', '{:e}'.format(startTime))
    print('Return time:', '{:e}'.format(returnTime))
    print('PONG', i, 'RTT: \n')
  except:
    print('Mesg sent:', 'Ping' + str(i))
    print('No Mesg rcvd')
    print('PONG', i, 'Request timed out \n')


print('Min RTT:')
print('Max RTT:')
print('Avg RTT:')
print('Packet Loss:')
print('Estimated RTT:')
print('Dev RTT:')
print('Timeout Interval:')
clientSocket.close()
