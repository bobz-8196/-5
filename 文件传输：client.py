import socket

serverName = 'LAPTOP-T2RC6NUO'
serverPort = 12000

# 创建UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

with open('file.txt', 'rb') as file:
    data = file.read()
clientSocket.sendto(data, (serverName, serverPort))

print("File sent")

clientSocket.close()
