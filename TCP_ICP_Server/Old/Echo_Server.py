import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('Starting server on %s port %s' % server_address, file=sys.stderr)

sock.bind(server_address)
sock.listen(1)

while True:
    print('Waiting for connection', file=sys.stderr)
    connection, client_address = sock.accept()

    try:
        print('Connection from', client_address, file=sys.stderr)
        while True:
            data = connection.recv(16)
            print('Received "%s"' % data, file=sys.stderr)
            if data:
                print('Sending data back', file=sys.stderr)
                connection.sendall(data)
            else:
                print('No more data from', client_address, file=sys.stderr)
                break
    finally:
        connection.close()
