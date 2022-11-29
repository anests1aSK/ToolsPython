#!/bin/python3
import socket
import threading

port = 9942
ip_addr = '0.0.0.0'

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip_addr,port))
    server.listen(5)
    print(f'[*] Listening on {ip_addr}:{port}')

    while True:
        client, address = server.accept() 
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket): 
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK')

print(__name__)
if __name__ == '__main__':
    main()