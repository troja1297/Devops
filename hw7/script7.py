class Router:
    ips = []

    def addip(self, ip, gatewayname):
        self.ips.append((ip, gatewayname))
        print("Добавляем ip-addres {} {}".format(ip, gatewayname))

    def removeip(self, ip):
        self.ips.remove(ip)

    def printip(self):
        for ip in self.ips:
            print(ip)


print("Введите ip-address:")
lint = input().upper().split(' ')
r = Router()
r.addip()
