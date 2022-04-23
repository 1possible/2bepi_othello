import json
import socket
import threading as th

class AICom:
    run = True

    def __init__(self,port,name,matricules):
        #rajouter exeption pour les int
        # name = "justUnTest"
        # matricules = ["12345", "67890"] #obliger d'avoir different matricule pour plusieur client
        #idée: faire des fonction pour verifier que les parametres sont dans le bon format
        self.port = port
        self.name = name
        self.matricules = matricules
        self.adresseServeurRunner = ('127.0.0.1', 3000)
        self.adresse = ('0.0.0.0',self.port)
        self.inscription()


    def inscription(self):
        with socket.socket() as sInscription:
            #faire fonction si jamais il arrive pas a ce connecter
            jsonDico = {"request": "subscribe", "port": self.port, "name": self.name, "matricules": self.matricules}
            sInscription.connect(self.adresseServeurRunner)
            invitation = json.dumps(jsonDico)
            sInscription.send(invitation.encode())
            reponseInscription = json.loads(sInscription.recv(2048).decode()) #mettre une gestion d'erreur ici
        if 'response' in reponseInscription.keys():
            if reponseInscription['response'] == 'ok':
                print(self.name + " inscription OK \n")
                self.threadEcoute = th.Thread(target = self.ecoute)
                self.threadEcoute.start()
            if reponseInscription['response'] == 'error':
                print(self.name + "inscriptionError : "+reponseInscription['error'])

    def ecoute(self):
        with socket.socket() as sAIServor:
            sAIServor.bind(self.adresse)
            while self.run:
                sAIServor.listen()
                clientRunner, adresseRunner = sAIServor.accept()
                messageServor = clientRunner.recv(2048).decode()
                try:
                    mServor = json.loads(messageServor)
                except:
                    print(self.name+ "imposible de convertir message en JSON")

                if 'request' in mServor.keys():
                    if mServor['request'] =='play':
                        clientRunner.send(json.dumps(self.play(mServor)).encode())
                    if mServor['request'] =='ping':
                        clientRunner.send(json.dumps({'response': 'pong'}).encode())
                        print(self.name+' PING PONG')
                #if 'reponse' in reponse.keys():
                #    if reponse['reponse'] == 'ok':
                #        print("OK")
        #        if reponse['reponse']== 'ping':
        #            self.s.send(json.dumps({'reponse':'pong'}).encode())
    def play(self,dicGame):
        #exemple dicGame
        #{'request': 'play',
        # 'lives': 3,
        # 'errors': [],
        # 'state': { 'players': ['prems', 'dems']
        #          , 'current': 0
        #          , 'board': [[28, 35], [27, 36]]}}
        #Abandon
        #{'response':'giveup'}
        #reponse
        #{
        #    "response": "move",
        #    "move": the_move_played, #doit etre un int
        #    "message": "Fun message"
        #}

        return {'response':'giveup'}

    def fin(self):
        self.run = False
        self.threadEcoute.join() #je sais pas si c'est une bonne idée de le mettre
        # car le theads s'arrete que quand un message arrive car il est bloqué a attendre un message