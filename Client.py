import socket
HOST = '127.0.0.1'
PORT = 50007
print("Client is running")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
data = input("Enter data to send to the server : ")
if data == "":
    data = "Hello World"
s.sendall(data.encode())
data = s.recv(1024)
print("Recieved from server : ",data.decode())
s.close()