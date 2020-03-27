from socket import *


serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

class RRValues:
    def __init__(self,name,htype,value,ttl,static):
        self.name = name
        self.htype = htype
        self.value = value
        self.ttl = ttl
        self.static = static

RRTable = []

Flag = True

count = 0

def countdown(num):
    print('In countdown')
    t = 60
    while t:       
        time.sleep(1)
        RRTable[num].ttl = t
        t -= 1
    RRTable.pop(num)
    count -= 1

def contains(sName):
    print(len(RRTable))
    for x in range(len(RRTable)):
        if RRTable[x].name is sName:
            return True
    return False

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
            for x in range(count):
                print(RRTable[x].name +  "\t\t" + RRTable[x].htype + "\t\t" + RRTable[x].value +'\t\t' + RRTable[x].ttl)
                         
            
        else:
            clientSocket.sendto(name.encode(), (serverName, serverPort))
            DNSResponse, serverAddress = clientSocket.recvfrom(2048)
            print(DNSResponse.decode())
            newV = RRValues(name,DNSQuery,DNSResponse.decode(),60,1)
            RRTable.insert(count,newV)
            print(len(RRTable))
            x = threading.Thread(target=countdown, args=(count,))
            x.start()
            count += 1

            #print('{the_name} has been added.'.format(the_name = name))
clientSocket.close()
