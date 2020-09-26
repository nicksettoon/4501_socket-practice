from socket import *

def start():
    #enters client UDP mode

    srvName = input('\nEnter the domain name of the server: ')
    srvPort = 12000

    cSocket = socket(AF_INET, SOCK_DGRAM)

    while True:
        mess = input("\nWhat sentence would you like capitalized?\n")

        if mess == "quit":
            print("Termination requested.")
            break

        cSocket.sendto(mess.encode(), (srvName, srvPort))
        modMess, srvAddr = cSocket.recvfrom(2048)

        print(modMess.decode())
        
    cSocket.close()