import socket

ports = [21,22,80,443,3306,25]

for port in ports:

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.3)
        code = client.connect_ex(("xxxxx.com.br", port))

        if code== 0:
                print("porta aberta", port)
        else:
                print("porta fechada", port)

