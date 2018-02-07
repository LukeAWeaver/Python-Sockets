from socket import *
import sys
serverPort = int(sys.argv[1])
bufferSize = 1024
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('server is ready to receive')
while True:
        connectionSocket, addr = serverSocket.accept()
        message = connectionSocket.recv(bufferSize)
        print("Message received from client:",message)
        message = message.upper()
        connectionSocket.send(message) #echo
        connectionSocket.close()
