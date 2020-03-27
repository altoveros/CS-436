from socket import*

qualcommRRTable = {
    "number1":
    {
        "TransactionID": "1",
        "Name": "www.qualcomm.com",
        "Type": "A",
        "Value": "104.86.224.205",
        "TTL": "",
        "Static" : "1"
        },
    "number2":
    {
        "TransactionID": "2",
        "Name": "qtiack12.qti.qualcomm.com",
        "Type": "A",
        "Value": "129.46.100.21",
        "TTL": "",
        "Static" : "1"
        }
    }


serverPort = 21000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ('The server is ready to receive')
while 1:
    message, localserverAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode()
    print(modifiedMessage)


    serverSocket.sendto(modifiedMessage.encode(), localserverAddress)
