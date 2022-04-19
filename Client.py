import json
import socket


class Client:
    def __init__(self):
        s = socket.socket()
        request = "subscribe"
        port = 8888
        name ="justUnTest"
        matricules = ["12345","67890"]
        jsonDico = {"request": request, "port":port, "name":name,"matricules":matricules}
        address = ('127.0.0.1', 3000)
        s.connect(address)
        invitation = json.dumps(jsonDico)
        print(invitation)
        s.send(invitation.encode())
        reponse = s.recv(2048).decode()
        print(reponse)
        s.close()
        print("s close")