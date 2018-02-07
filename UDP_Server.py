from socket import *
import sys
serverPort = int(sys.argv[1])
bufferSize = 1024
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print('server is ready to receive')
while True:
        message, clientAddress = serverSocket.recvfrom(1024)
        print("Message received from client:",message)
        message = message.upper()
        serverSocket.sendto(message, clientAddress)
