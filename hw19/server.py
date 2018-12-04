import socket
dnsList = []
bufDnsList = []

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    if not data or data == 'stop':
        break
    else:
        arr = data.decode().split(' ')
        command = arr[0]
        args = arr[1]
        ipDomain = args.split(':')

        if command == 'add':
            dnsList.append([ipDomain[0], ipDomain[1]])
            print('add {} {}'.format(ipDomain[0], ipDomain[1]))
        elif command == 'redf':
            print('redf')
            i = 0
            for s in dnsList:
                i += 1
                if ipDomain[1] == s[1]:
                    bufDnsList = dnsList
                    bufDnsList[i] = ipDomain
        dnsList = bufDnsList
        print(dnsList, print(bufDnsList))
        conn.close()

