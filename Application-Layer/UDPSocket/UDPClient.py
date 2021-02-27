from socket import *

serverName = '115.159.63.213'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input sentense:')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
