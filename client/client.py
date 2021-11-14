import socket
FORMAT = "UTF8"
serverAdd = input("Server Add:")
serverPort = int(input("Server Port:"))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)


try:
    client.connect((serverAdd, serverPort))

    print("Ket noi thanh cong")


    while(1):
        msg = client.recv(1024).decode(FORMAT)
        msg2 = client.recv(1024).decode(FORMAT)
        print("Username: ", msg)
        print("Pass:", msg2)
        msg = input('Nhập tin nhắn: ')
        client.send(msg.encode(FORMAT))

        if(msg == 'x'):
            break
except:  # Bắt trường hợp server bị đóng
    print("Error")
#.......

client.close()

input()
