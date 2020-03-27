from socket import *

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Enter the host or domain name: ')
message2 = input('Enter the type of DNS query (0. A, 1. AAAA, 2. CNAME, 3. NS: ')

serverName = message

clientSocket.sendto(message2.encode(), serverName, serverPort))

modifiedResponse, serverAddress = clientSocket.recvfrom(2048)

print modifiedResponse.decode()
clientSocket.close()


