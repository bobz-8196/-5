import socket
import os
import zipfile

serverPort = 12000

# 创建UDP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定服务器地址和端口
serverSocket.bind(('', serverPort))

print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    directory = message.decode()
    if os.path.isdir(directory):
        with zipfile.ZipFile('received.zip', 'w') as zipf:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    zipf.write(os.path.join(root, file))
        with open('received.zip', 'rb') as file:
            data = file.read()
        serverSocket.sendto(data, clientAddress)
        print("Directory sent")
    else:
        print("Directory not found")
