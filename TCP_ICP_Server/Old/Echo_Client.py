import socket
import sys

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to socket
server_address = ('localhost', 10000)
print('Connecting to %s port %s' % server_address, file=sys.stderr)
sock.connect(server_address)

try:
    # Send
    message = "Insert Message:".encode()  # Encode the message to bytes
    print('Sending %s' % message.decode())
    sock.sendall(message)

    # Response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('Received "%s"' % data.decode(), file=sys.stderr)  # Corrected spelling of "received"
finally:
    print('Closing socket', file=sys.stderr)
    sock.close()

