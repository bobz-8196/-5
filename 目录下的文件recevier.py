import socket
import os

serverPort = 12000

# 创建UDP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定服务器地址和端口
serverSocket.bind(('', serverPort))

print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    filename = message.decode()
    if os.path.isfile(filename):
        with open(filename, 'rb') as file:
            data = file.read()
        serverSocket.sendto(data, clientAddress)
        print("File sent")
    else:
        print("File not found")
