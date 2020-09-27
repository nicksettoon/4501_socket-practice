from socket import *

def start():
    #enters UDP server mode
    srvPort = 12000

    srvSocket = socket(AF_INET, SOCK_DGRAM)
    srvSocket.bind(("", srvPort))

    while True:
        print("Server is waiting for packets.\n")
        mess, cAddr = srvSocket.recvfrom(2048)
        # print("client addr: ", cAddr, "\n")
        mess = mess.decode()

        if mess == "quit":
            print("Client requested termination.")
            srvSocket.sendto("closing".encode(), cAddr)
            srvSocket.close()
            return False

        print("Server received: \n", mess)

        modMess = mess.upper()

        print("Sending: \n", modMess)

        srvSocket.sendto(modMess.encode(), cAddr)
        print("Sent")
