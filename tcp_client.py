from socket import *

def start():
    #enters client TCP mode

    # srvName = input('\nEnter the domain name of the server: ')
    srvName = "settoon.info"
    srvPort = 12000

    cSocket = socket(AF_INET, SOCK_STREAM)
    cSocket.connect((srvName, srvPort))

    while True:
        sent = input("\nWhat sentence would you like capitalized?\n")

        if sent == "back":
            print("Termination requested.")
            break

        cSocket.send(sent.encode())
        modSent = cSocket.recv(1024)

        print("Server returned: ", modSent.decode(), "\n")
        
    cSocket.close()