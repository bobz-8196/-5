import socket
import os
import threading

serverPort = 12002

# 创建UDP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定服务器地址和端口
serverSocket.bind(('', serverPort))

print("The server is ready to receive")

def handle_client(clientAddress, message):
    filename = message.decode()
    if os.path.isfile(filename):
        with open(filename, 'rb') as file:
            data = file.read()
        serverSocket.sendto(data, clientAddress)
        print("File sent to", clientAddress)
    else:
        print("File not found")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    threading.Thread(target=handle_client, args=(clientAddress, message)).start()
