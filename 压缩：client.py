import socket
import os
import zipfile

serverName = 'LAPTOP-T2RC6NUO'
serverPort = 12000

# 创建UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

directory = input('Input directory name: ')
clientSocket.sendto(directory.encode(), (serverName, serverPort))

data, serverAddress = clientSocket.recvfrom(2048)
with open('received.zip', 'wb') as file:
    file.write(data)
print("Directory received")

with zipfile.ZipFile('received.zip', 'r') as zipf:
    zipf.extractall()

clientSocket.close()
