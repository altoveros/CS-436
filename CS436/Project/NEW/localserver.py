from socket import *
import time
import logging
import threading

class RRValues:
    def __init__(self,name,htype,value,ttl,static):
        self.name = name
        self.htype = htype
        self.value = value
        self.ttl = ttl
        self.static = static

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

count = 0
tempRR = []

def changeCount(n):
    global count
    count += n

def contains(sName):
    return False
    for x in range(len(tempRR)):
        if tempRR[x].name == sName:
            return True
    return False

def countdown(Table):
    t = 60
    while t:       
        time.sleep(1)
        Table.ttl = t
        t -= 1
    tempRR.pop(0)
    changeCount(-1)
    return

serverPort = 15000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ('The server is ready to receive')
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    DNSQuery, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode()
    DNSModified = DNSQuery.decode()
    Flag = True
    for item in RRTable.values():
        if(item['Name'] == modifiedMessage and item['Type'] == DNSModified):
            print("Name Found! It's value is " + item['Value'])
            modifiedMessage = item['Value']
            print("It is now modified " + modifiedMessage)
            Flag = False
    if Flag is True:       
        if contains(modifiedMessage):
            print("\n")
            print(modifiedMessage + " already exists, here is the current table")
            print("\n")
            print("Name\t\tType\t\tValue\t\tTTL\t\tStatic")
            for x in range(len(tempRR)):
                print(tempRR[x].name +  "\t\t" + tempRR[x].htype + "\t\t" + tempRR[x].value +'\t\t' + str(tempRR[x].ttl))
        elif('viasat.com' in modifiedMessage):
            print(modifiedMessage + " does not exist in local server table, checking other servers...")
            serverSocket.sendto(modifiedMessage.encode(), ('localhost', 22000))
            serverSocket.sendto(DNSModified.encode(), ('localhost', 22000))
            DNSResponse, serverAddress = serverSocket.recvfrom(2048)
            print(DNSResponse.decode())
            newV = RRValues(modifiedMessage,DNSModified,DNSResponse.decode(),60,1)
            tempRR.append(newV)
            x = threading.Thread(target=countdown, args=(tempRR[count],))
            x.start()
            changeCount(1)
            modifiedMessage = DNSResponse.decode()
        else:#(modifiedMessage.find('qualcomm.com')):
            print(modifiedMessage + " does not exist in local server table, checking other servers...")
            serverSocket.sendto(modifiedMessage.encode(), ('localhost', 21000))
            serverSocket.sendto(DNSModified.encode(), ('localhost', 21000))
            DNSResponse, serverAddress = serverSocket.recvfrom(2048)
            print(DNSResponse.decode())
            newV = RRValues(modifiedMessage,DNSModified,DNSResponse.decode(),60,1)
            tempRR.append(newV)
            x = threading.Thread(target=countdown, args=(tempRR[count],))
            x.start()
            changeCount(1)
            modifiedMessage = DNSResponse.decode()
            
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
