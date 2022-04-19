import json
import socket
import threading as th

class Client:
    def __init__(self):
        self.s = socket.socket()
        request = "subscribe"
        port = 8888
        name ="justUnTest"
        matricules = ["12345","67890"]
        jsonDico = {"request": request, "port":port, "name":name,"matricules":matricules}
        address = ('127.0.0.1', 3000)
        self.s.connect(address)
        invitation = json.dumps(jsonDico)
        self.s.send(invitation.encode())
        threadEcoute = th.Thread(target = self.ecoute)
        threadEcoute.start()
    def ecoute(self):
        reponseServor = self.s.recv(2048).decode()
        reponse = json.loads(reponseServor)



    def fin(self):
        self.s.close()