import socket
import sys
import logging

# Logging configuration
logging.basicConfig(filename='Chat_log.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('Starting server on %s port %s' % server_address, file=sys.stderr)
logging.info('Starting server on %s port %s' % server_address)

sock.bind(server_address)
sock.listen(1)

while True:
    print('Waiting for connection', file=sys.stderr)
    logging.info('Waiting for connection')
    connection, client_address = sock.accept()

    try:
        print('Connection from', client_address, file=sys.stderr)
        logging.info('Connection from %s', client_address)
        while True:
            data = connection.recv(32)
            print('Received "%s"' % data, file=sys.stderr)
            logging.info('Received "%s"', data)
            if data:
                print('Sending data back', file=sys.stderr)
                logging.info('Sending data back')
                connection.sendall(data)
                print('Sent "%s"' % data, file=sys.stderr)
                logging.info('Sent "%s"', data)
            else:
                print('No more data from', client_address, file=sys.stderr)
                logging.info('No more data from %s', client_address)
                break
    finally:
        connection.close()
