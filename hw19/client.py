import socket

print("Additing: ADD google.com:123.231.123.1")
print("Redifinition: REDF YOUHOST:YOUIP")
print("stop - exit")

sock = socket.socket()
sock.connect(('localhost', 9090))
while True:
    message = input()
    message.lower()
    if message == 'stop':
        sock.close()
        break
    else:
        sock.send(message.encode())

