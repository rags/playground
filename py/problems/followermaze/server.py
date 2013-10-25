#!/usr/bin/python
import socket
from threading import Thread
from event_handler import EventHandler
from message_queue import MessageQueue
from user_network import UserNetwork

users = {}
queue = MessageQueue()
event_handler = EventHandler(users, UserNetwork())

def bind_server(port, queue_len=1):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('localhost', port))
    serversocket.listen(queue_len)
    return serversocket
    
def event_listener(port=9090):
    serversocket = bind_server(port)
    data = None
    clientsocket = None
    while True:
        try:
            if not data:
                if clientsocket:
                    print("Event stream has stopped. Press Ctrl-C to stop the server")
                    clientsocket.close()
                clientsocket, _ = serversocket.accept()
            else:
                queue.push_data_stream(data)
            data = clientsocket.recv(1024)
        except:
            clientsocket, _ = serversocket.accept()
    
def user_register(port=9099):
    serversocket = bind_server(port, 5)
    while True:
        clientsocket, _ = serversocket.accept()
        data = clientsocket.recv(1024)
        if not data:
            clientsocket.close();
        else:
            users[data.strip()] = clientsocket
            print("Add user", data)

def worker():
    while True:
        id, data = queue.pop()
        event_handler.handle(data)
    
def main():
    Thread(target=user_register).start()
    Thread(target=event_listener).start()
    Thread(target=worker).start()
    

if __name__ == '__main__':
    main()
