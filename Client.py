import math
import time
from socket import *

host = '10.0.0.2'
port = 12000
timeout = 1  # in seconds

alpha = 0.125
beta = 0.25
# Creates UDP client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# sets socket timeout to 1 second
clientSocket.settimeout(timeout)
# array to hold rtt
rtt_stats = []
for i in range(1, 11):
    data = 'Ping {}'.format(str(i))

    try:
        # Sent time
        sendTime = time.time()
        # Send the UDP packet with ping message
        clientSocket.sendto(data.encode(), (host, port))
        # Receive server response
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        # Received time
        returnTime = time.time()
        # calculate RTT
        rtt = (returnTime - sendTime) * 1000
        # Add rtt to array
        rtt_stats.append(rtt)

        print('Mesg sent:', data)
        print('Mesg rcvd:', modifiedMessage.decode())
        print('Start time:', '{:e}'.format(sendTime))
        print('Return time:', '{:e}'.format(returnTime))
        print('PONG {} RTT: {}ms'.format(i, rtt))
    except:
        print('PONG', i, 'Request timed out \n')
        continue
clientSocket.close()

print('Min RTT: {}'.format(min(rtt_stats)))
print('Max RTT: {}'.format(max(rtt_stats)))
print('Avg RTT: {}'.format(sum(rtt_stats) / len(rtt_stats)))
print('Packet Loss:')
print('Estimated RTT:')
print('Dev RTT:')
print('Timeout Interval:')
