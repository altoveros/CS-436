from socket import *
import time
import logging
import threading

serverName = 'localhost'
serverPort = 15000
clientSocket = socket(AF_INET, SOCK_DGRAM)

class RRValues:
    def __init__(self,name,htype,value,ttl,static):
        self.name = name
        self.htype = htype
        self.value = value
        self.ttl = ttl
        self.static = static

Flag = True

count = 0

def changeCount(n):
    global count
    count += n

def countdown(Table,count):
    t = 5
    while t:       
        time.sleep(1)
        Table.ttl = t
        t -= 1
    RRTable.pop(0)
    changeCount(-1)
    return

def contains(sName):
    for x in range(len(RRTable)):
        if RRTable[x].name == sName:
            return True
    return False

RRTable = []

while Flag:
    
    name = input('Enter the host or domain name (Exit to quit program): ' )

    if name == "exit":
        Flag = False
    else:
        DNSQuery = input('Enter the type of DNS query (0. A, 1. AAAA, 2. CNAME, 3. NS: )')

        # Check to see if the name is already in the dictionary.
        if contains(name):
            print("\n")
            print(name + " already exists, here is the current table")
            print("\n")
            print("Name\t\tType\t\tValue\t\tTTL\t\tStatic")
            for x in range(len(RRTable)):
                print(RRTable[x].name +  "\t\t" + RRTable[x].htype + "\t\t" + RRTable[x].value +'\t\t' + str(RRTable[x].ttl))
                         
            
        else:
            clientSocket.sendto(name.encode(), (serverName, serverPort))
            clientSocket.sendto(DNSQuery.encode(), (serverName, serverPort))
            DNSResponse, serverAddress = clientSocket.recvfrom(2048)
            print(DNSResponse.decode())
            newV = RRValues(name,DNSQuery,DNSResponse.decode(),5,1)
            RRTable.append(newV)
            x = threading.Thread(target=countdown, args=(RRTable[count],count))
            x.start()
            changeCount(1)

            #print('{the_name} has been added.'.format(the_name = name))
clientSocket.close()
