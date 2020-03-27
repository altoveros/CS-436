from socket import *

  clientSocket = socket(AF_INET, SOCK_DGRAM)

RRTable{}
count = 1

message = input('Enter the host or domain name: ')


message2 = input('Enter the type of DNS query (0. A, 1. AAAA, 2. CNAME, 3. NS: ')

clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())

if not message in RRTable.values():
  RRTable[key].append(count)
  RRTable[key].append(message)
  RRTable[key].append(message2)
  RRTable[key].append(serverAddress)
  RRTable[key].append(60)
  RRTable[key].append()
  count += 1

clientSocket.close()


