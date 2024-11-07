import socket

serverName = 'LAPTOP-T2RC6NUO'
serverPort = 12001

# 创建UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

filename = input('Input file name: ')
clientSocket.sendto(filename.encode(), (serverName, serverPort))

data = b''
while True:
    chunk, serverAddress = clientSocket.recvfrom(1024)
    if not chunk:
        break
    data += chunk
with open('received_file', 'wb') as file:
    file.write(data)
print("File received")

clientSocket.close()
