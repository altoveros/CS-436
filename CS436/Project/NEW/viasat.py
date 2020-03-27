from socket import *

viasatRRTable = {
    "number1":
    {
        "TransactionID": "1",
        "Name": "www.viasat.com",
        "Type": "A",
        "Value": "8.37.96.179",
        "TTL": "",
        "Static" : "1"
        },


serverPort = 22000
ServerSocket = socket(AF_INET, SOCK_DGRAM)
ServerSocket.bind(('', serverPort))
print ('The server is ready to receive')
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    DNSQuery, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode()
    DNSModified = DNSQuery.decode()
    print(DNSModified)
    print(modifiedMessage)
    for item in viasatRRTable.values():
        if(item['Name'] == modifiedMessage and item['Type'] == DNSModified):
            print("Name Found! It's value is " + item['Value'])
            modifiedMessage = item['Value']
            print("It is now modified " + modifiedMessage)

    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
