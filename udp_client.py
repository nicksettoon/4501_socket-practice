from socket import *

def start():
    #enters client UDP mode

    # srvName = input('\nEnter the domain name of the server: ')
    srvName = "settoon.info"
    srvPort = 12000

    cSocket = socket(AF_INET, SOCK_DGRAM)
    # cSocket.bind(('', 2515))

    while True:
        # print(cSocket.getsockname())
        mess = input("\nWhat sentence would you like capitalized?\n")

        if mess == "back":
            print("Going to previous menu.")
            break

        cSocket.sendto(mess.encode(), (srvName, srvPort))
        modMess, srvAddr = cSocket.recvfrom(2048)

        modMess = modMess.decode()
        if modMess == "closing":
            break

        print(modMess)
        
    cSocket.close()