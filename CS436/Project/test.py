from socket import *

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Enter the host or domain name: ')



message2 = input('Enter the type of DNS query (0. A, 1. AAAA, 2. CNAME, 3. NS: ')

clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print (modifiedMessage.decode())


clientSocket.close()


