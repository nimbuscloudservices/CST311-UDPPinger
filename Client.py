import time
from socket import *

host = '10.0.0.2'
port = 12000
timeout = 1  # in seconds
# used for stats
alpha = 0.125
beta = 0.25
estimatedRTT = 0
devRTT = 0
# Creates UDP client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
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
        # sets socket timeout to 1 second
        clientSocket.settimeout(timeout)
        # calculate RTT
        rtt = (returnTime - sendTime) * 1000
        # Add rtt to array
        rtt_stats.append(rtt)
        if i == 1:
            estimatedRTT = rtt
            devRTT = rtt / 2
        else:
            estimatedRTT = ((1 - alpha) * estimatedRTT) + (alpha * rtt)
            devRTT = ((1 - beta) * devRTT) + (beta * abs(rtt - estimatedRTT))

        print('Mesg sent:', data)
        print('Mesg rcvd:', modifiedMessage.decode())
        print('Start time:', '{:e}'.format(sendTime))
        print('Return time:', '{:e}'.format(returnTime))
        print('PONG {} RTT: {} ms\n'.format(i, rtt))
    except:
        print('PONG', i, 'Request timed out \n')
        continue
clientSocket.close()

# Calculate Stats
# Packet Loss
loss = ((10 - len(rtt_stats)) / 10) * 100
# Timeout interval value
timeoutInterval = estimatedRTT + (4 * devRTT)
# Average
avg = sum(rtt_stats) / len(rtt_stats)

# Print out Stats
print('-------------- Ping Stats ---------------')
print('Min RTT: {}'.format(min(rtt_stats)))
print('Max RTT: {}'.format(max(rtt_stats)))
print('Avg RTT: {}'.format(avg))
print('Packet Loss: {}%'.format(loss))
print('Estimated RTT: {} ms'.format(estimatedRTT))
print('Dev RTT: {} ms'.format(devRTT))
print('Timeout Interval: {} ms'.format(timeoutInterval))
print('-----------------------------------------')
