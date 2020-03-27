from socket import *

RRTable = {
    "number1":
    {
        "TransactionID": "1",
        "Name": "www.csusm.edu",
        "Type": "A",
        "Value": "144.37.5.45",
        "TTL": "",
        "Static" : "1"
        },
    "number2":
    {
        "TransactionID": "2",
        "Name": "cc.csusm.edu",
        "Type": "A",
        "Value": "144.37.5.117",
        "TTL": "",
        "Static" : "1"
        },
    "number3":
    {
        "TransactionID": "3",
        "Name": "cc1.csusm.edu",
        "Type": "CNAME",
        "Value": "cc.csusm.edu",
        "TTL": "",
        "Static" : "1"
        },
    "number4":
    {
        "TransactionID": "4",
        "Name": "cc1.csusm.edu",
        "Type": "A",
        "Value": "144.37.5.118",
        "TTL": "",
        "Static" : "1"
        },
    "number5":
    {
        "TransactionID": "5",
        "Name": "my.csusm.edu",
        "Type": "A",
        "Value": "144.37.5.150",
        "TTL": "",
        "Static" : "1"
        },
    "number6":
    {
        "TransactionID": "6",
        "Name": "www.qualcomm.com",
        "Type": "NS",
        "Value": "dns.qualcomm.com",
        "TTL": "",
        "Static" : "1"
        },
    "number7":
    {
        "TransactionID": "7",
        "Name": "viasat.com",
        "Type": "NS",
        "Value": "dns.viasat.com",
        "TTL": "",
        "Static" : "1"
        }
    }




serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ('The server is ready to receive')
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    DNSQuery, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode()
    DNSModified = DNSQuery.decode()
    print(DNSModified)
    print(modifiedMessage)
    for item in RRTable.values():
        if(item['Name'] == modifiedMessage and item['Type'] == DNSModified):
            print("Name Found! It's value is " + item['Value'])
            modifiedMessage = item['Value']
            print("It is now modified " + modifiedMessage)
        else:
            serverSocket.sendto(modifiedMessage.encode(), ('qualcommserver', 21000))
            

    
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
