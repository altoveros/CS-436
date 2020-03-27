from socket import *


serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

RRTableName = []
RRTableType = []
RRTableValue = []
RRTTLValue = []
RRStaticValue = []


count = 1

Flag = True


while Flag:
    
    name = input('Enter the host or domain name (Exit to quit program): ' )

    if name == "exit":
        Flag = False
    else:
        DNSQuery = input('Enter the type of DNS query (0. A, 1. AAAA, 2. CNAME, 3. NS: )')

        # Check to see if the name is already in the dictionary.
        if name in RRTableName:
            print("\n")
            print(name + " already exists, here is the current table")
            print("\n")
            print("Name\t\tType\t\tValue\t\tTTL\t\tStatic")
            for x in range(len(RRTableName)):
                print(RRTableName[x] +  "\t\t" + RRTableType[x] + "\t\t" + RRTableValue[x])
               
            
            
        else:
            clientSocket.sendto(name.encode(), (serverName, serverPort))
            DNSResponse, serverAddress = clientSocket.recvfrom(2048)
            print(DNSResponse.decode())

            #print('{the_name} has been added.'.format(the_name = name))
clientSocket.close()
