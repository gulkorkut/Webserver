from socket import *
import sys

# Create a server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        # Receive message from client
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]

        # Open and read the requested file
        f = open(filename[1:])
        outputdata = f.read()

        # Send HTTP response header and requested file content to client
        header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: ' + str(len(outputdata)) + '\r\n\r\n'
        connectionSocket.send(header.encode())
        for i in range(len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        # Close client socket
        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        error_header = 'HTTP/1.1 404 Not Found\r\n\r\n'
        error_message = '<html><head></head><body><h1>404 Not Found</h1></body></html>'
        connectionSocket.send((error_header + error_message).encode())

        # Close client socket
        connectionSocket.close()

# Close server socket
serverSocket.close()
