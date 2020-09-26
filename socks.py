import sys
import udp_client as udpc
import udp_srv as udps
import tcp_client as tcpc
import tcp_srv as tcps

if __name__ == "__main__":
    args = sys.argv
    
    while True:
        mode = input("Which mode do you want?\n1. UDP\n2. TCP\nPlease input 1 or 2:\t")

        if mode == "1":
            if args[1] == "-s":
                tcps.start()
            elif args[1] == "-c":
                tcpc.start()
            break

        elif mode == "2":
            if args[1] == "-s":
                udps.start()
            elif args[1] == "-c":
                udpc.start()
            break
        else:
            print("Invalid input, try again please.")
