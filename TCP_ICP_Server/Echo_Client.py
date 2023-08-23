import socket
import sys

def send_receive_messages():
    # Create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to socket
    server_address = ('localhost', 10000)
    print('Connecting to %s port %s' % server_address, file=sys.stderr)
    sock.connect(server_address)

    try:
        while True:  # Keep looping to send/receive messages
            # Send
            message = input("Enter message (or 'exit' to quit): ")
            if message.lower() == 'exit':
                break

            message_bytes = message.encode()
            print('Sending %s' % message)
            sock.sendall(message_bytes)

            # Response
            amount_received = 0
            amount_expected = len(message_bytes)

            while amount_received < amount_expected:
                data = sock.recv(32)
                amount_received += len(data)
                print('Received "%s"' % data.decode(), file=sys.stderr)

    finally:
        print('Closing socket', file=sys.stderr)
        sock.close()

if __name__ == "__main__":
    send_receive_messages()

