import socket

serverName = 'LAPTOP-T2RC6NUO'
serverPort = 12000

# 创建UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

filename = input('Input file name: ')
clientSocket.sendto(filename.encode(), (serverName, serverPort))

data, serverAddress = clientSocket.recvfrom(2048)
with open('received_file', 'wb') as file:
    file.write(data)
print("File received")

clientSocket.close()
