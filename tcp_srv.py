from socket import *

def start():
    #enters UDP server mode
    srvPort = 12000

    srvSocket = socket(AF_INET, SOCK_STREAM)
    srvSocket.bind(("", srvPort))
    srvSocket.listen(1)
    print("Server is waiting for connection.\n")
    clientConnSocket, cAddr = srvSocket.accept()

    while True:
        print("Server is waiting for packets.\n")
        sent = clientConnSocket.recv(1024).decode()
        if sent is None:
            break

        if sent == "end":
            clientConnSocket.close()
            return True
        elif sent == "quit":
            print("Client requested termination.")
            clientConnSocket.close()
            srvSocket.close()
            return False

        print("Server received: \n", sent)

        capSent = sent.upper()

        print("Sending: \n", capSent)

        clientConnSocket.send(capSent.encode())
        print("Sent")
