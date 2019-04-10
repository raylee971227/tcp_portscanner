# Raymond Lee
# Port Scanner Project
# ECE-303: Communication Networks
# Prof. Shivam Mevawala

import sys
from PortScanner import PortScanner

def main():
    argc = len(sys.argv)
    start_port = 1
    end_port = 1024
    # Check for proper usage
    if (argc == 1 or argc != 4):
        print('Error: Proper usage is \"python portscanner.py -host [-p 15:25]\"')
        return -1
    # Correct usage
    elif argc == 4:
        if sys.argv[2] == '-p':
            start_port = int(sys.argv[3].split(':')[0])
            end_port = int(sys.argv[3].split(':')[1])
        else:
            print('Error: Proper usage is \"python portscanner.py -host [-p 15:25]\"')

    # Get host name
    target = sys.argv[1]

    #initialize port scanner
    scanner = PortScanner(target, start_port, end_port)
    try:
        scanner.run()
    except KeyboardInterrupt:
        print('Ctrl + C encountered. Exitting...')
        sys.exit(-1)


main()