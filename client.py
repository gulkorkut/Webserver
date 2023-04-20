import sys
from socket import *

# Get the server hostname, port and filename from command line arguments
host = sys.argv[1]
port = int(sys.argv[2])
filename = sys.argv[3]

# Create a TCP client socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to the server
clientSocket.connect((host, port))

# Construct and send the HTTP request message
requestMessage = 'GET /' + filename + ' HTTP/1.1\r\nHost: ' + host + ':' + str(port) + '\r\n\r\n'
clientSocket.send(requestMessage.encode())

# Receive the HTTP response message (header and content)
responseMessage = ''
while True:
    response = clientSocket.recv(4096)
    responseMessage += response.decode()
    if '\r\n\r\n' in responseMessage:
        break

# Print the HTTP response message header
print(responseMessage[:responseMessage.index('\r\n\r\n')])

# Print the HTTP response message content (if any)
if '\r\n\r\n' in responseMessage:
    content = responseMessage[responseMessage.index('\r\n\r\n') + 4:]
    print(content)

# Close the client socket
clientSocket.close()




