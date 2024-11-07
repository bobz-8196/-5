import socket

serverPort = 12000

# 创建UDP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定服务器地址和端口
serverSocket.bind(('', serverPort))

print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    with open('received.txt', 'wb') as file:
        file.write(message)
    print("File received")
