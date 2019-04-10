# Raymond Lee
# Port Scanner Project
# ECE-303: Communication Networks
# Prof. Shivam Mevawala

import socket
import threading
from queue import Queue
import os

class PortScanner:
    def __init__(self, host, start, end):
        self.host = host
        self.start = start
        self.end = end + 1
        self.q = Queue()
        # List of default protocol port numberse
        self.dictionary = {
            20: "FTP",
            21: "FTP",
            22: "SSH",
            23: "TELNET",
            25: "SMTP",
            52: "DNS",
            80: "HTTP",
            109: "POP2",
            110: "POP3",
            220: "IMAP",
            427: "SLP",
            443: "HTTPS",
            993: "IMAPS",
            995: "POP3S"
        }

    def port_scan(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # s.settimeout(.5)
        try:
            connection = s.connect_ex((self.host, port))
            with threading.Lock():
                # if port in self.dictionary:
                print('port #', port, 'is open with {}'.format(socket.getservbyport(port)))
                    # print('port #', port, 'is open running', self.dictionary[port], 'protocol!')
                # else:
                #     print('port #', port, 'is open!')
            connection.close

        except socket.gaierror:
            print('Hostname:', self.host ,'could not be resolved!')
            os._exit(-1)

        except socket.error:
            print('Could not connect to server!')
            os._exit(-1)

    #Default Exception handler
        except:
            pass

    def threader(self):
        while True:
            worker = self.q.get()
            self.port_scan(worker)
            self.q.task_done()

    def run(self):
        for x in range(50):
            t = threading.Thread(target=self.threader)
            t.daemon = True
            t.start()

        for worker in range(self.start, self.end):
            self.q.put(worker)
        
        self.q.join()
        print('Scan Finished!')
