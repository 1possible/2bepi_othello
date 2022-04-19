import json
import socket
import threading as th

class Client:
    run = True

    def __init__(self,port):
        #rajouter exeption pour les int
        self.s = socket.socket()
        request = "subscribe"
        name = "justUnTest"
        matricules = ["12345", "67890"]
        self.config(request,port,name,matricules)

    def config(self,request,port, name,matricules):
        jsonDico = {"request": request, "port":port, "name":name,"matricules":matricules}
        address = ('127.0.0.1', 3000)
        self.connect(address , jsonDico)

    def connect(self,adresseServor, jsonDico):
        self.s.connect(adresseServor)
        invitation = json.dumps(jsonDico)
        self.s.send(invitation.encode())
        threadEcoute = th.Thread(target = self.ecoute)
        threadEcoute.start()

    def ecoute(self):
        while self.run:
            reponseServor = self.s.recv(2048).decode()
            #Attenstion parfois il est vide
            if reponseServor is not '':
                reponse = json.loads(reponseServor)
                print(reponse)
            else :
                reponse = {}
            if 'reponse' in reponse.keys():
                if reponse['reponse'] == 'ok':
                    pass
                if reponse['reponse']== 'ping':
                    self.s.send(json.dumps({'reponse':'pong'}).encode())
            if 'request' in reponse.keys():
                if reponse['request'] =='play':
                    self.s.send(json.dumps({'reponse':'giveup'}).encode())
    def fin(self):
        self.s.close()