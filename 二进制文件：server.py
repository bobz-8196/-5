import socket
import os

serverPort = 12001

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
        # 分割文件数据为多个数据报
        chunks = [data[i:i+1024] for i in range(0, len(data), 1024)]
        for chunk in chunks:
            serverSocket.sendto(chunk, clientAddress)
        print("File sent")
    else:
        print("File not found")
