from socket import *
import sys
serverIP = sys.argv[1]
serverPort = int(sys.argv[2])
bufferSize = 1024
print("UDP server IP address:", serverIP)
print ("UDP Server port number:", serverPort)
while True:
        print("CTRL-C to close program")
        message = raw_input('Input lowercase sentence:')
        print("Message to be sent to server",message)
        clientSocket = socket(AF_INET,SOCK_STREAM) #UDP
        clientSocket.connect((serverIP,serverPort))
        clientSocket.send(message)
        recvMessage = clientSocket.recv(bufferSize)
        print("Message received from server:",recvMessage)
        clientSocket.close()
