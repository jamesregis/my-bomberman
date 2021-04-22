# -*- coding: utf-8 -*-
# Bomberman in python

import select
import socket
import sys

def create_tcp_server(port):
    host = ''
    port = 50000
    backlog = 5
    size = 1024
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host,port))
    server.listen(backlog)
    iinput = [server,sys.stdin]
    running = 1
    while running:
        inputready,outputready,exceptready = select.select(iinput,[],[]) 
        for s in inputready:

            if s == server:
                # handle the server socket
                client, address = server.accept()
                iinput.append(client)

            elif s == sys.stdin:
                # handle standard input
                junk = sys.stdin.readline()
                running = 0

            else:
                # handle all other sockets
                data = s.recv(size)
                if data:
                    #print 'from ', address
                    #print 'type ', type(address)
                    #print 'data ', data
                    # TODO :
                    # send to everybody except sender
                    for i in iinput[2::] :
                        print i
                        if i != s:
                            i.send(data)

                else:
                    s.close()
                    iinput.remove(s)
    server.close()  


if __name__== "__main__":
    create_tcp_server(5000)
