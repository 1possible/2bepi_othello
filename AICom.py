import json
import socket
import threading as th

import argparse

import AIStrat
import First_strategy

withThread= True

class AICom:
    run = True

    def __init__(self,port,name,strat ="i",matricules=['21258','20242'],servor='127.0.0.1'):
        #fonction qui initialise les variables du programme et lance l'inscription
        # port = le port sur lequel le program va écoute pour les request du serveur
        # name = "justUnTest"
        # matricules = ["12345", "67890"] #obliger d'avoir different matricule pour plusieur client
        # strat = char qui dit quelle strategie utilise (plus d'info README)
        #           "a"=aleatoire
        #           "m"=MinMax
        #           "i"=negamax avec profondeur iterative
        #           "f"=firstcoup
        #           "n"=strategie du moindre coup
        #servor = adresse du serveur championshipRunnner
        #idée: faire des fonction pour verifier que les parametres sont dans le bon format
        self.port = port
        self.name = name
        self.matricules = matricules
        self.strat =strat
        self.adresseServeurRunner = (servor,3000)
        self.adresse = ('0.0.0.0',self.port)
        if self.strat != "t":
            self.inscription()


    def inscription(self):
        #fonction qui inscrit le programme à l'adresse (adresseServeurRunner)
        # si il arrive a s'inscrire il lance la fonction "ecoute"
        with socket.socket() as sInscription:
            #idée: faire fonction si jamais il arrive pas a ce connecter
            jsonDico = {"request": "subscribe", "port": self.port, "name": self.name, "matricules": self.matricules}
            sInscription.connect(self.adresseServeurRunner)
            invitation = json.dumps(jsonDico)
            sInscription.send(invitation.encode())
            reponseInscription = json.loads(sInscription.recv(2048).decode()) #mettre une gestion d'erreur ici
        if 'response' in reponseInscription.keys():
            if reponseInscription['response'] == 'ok':
                print(self.name + " inscription OK \n")
                if withThread:
                    self.threadEcoute = th.Thread(target = self.ecoute)
                    self.threadEcoute.start()
                else:
                    self.ecoute()
            if reponseInscription['response'] == 'error':
                print(self.name + "inscriptionError : "+reponseInscription['error'])

    def ecoute(self):
        #fonction qui s'occupe des request envoye par le serveur
        #repond a ping par pong
        #lance play quand il recoit la requet move
        with socket.socket() as sAIServor:
            sAIServor.settimeout(1)
            sAIServor.bind(self.adresse)
            sAIServor.listen()
            while self.run:
                try:
                    clientRunner, adresseRunner = sAIServor.accept()
                    messageServor = clientRunner.recv(2048).decode()
                    try:
                        mServor = json.loads(messageServor)
                    except:
                        print('ERROR: '+self.name+ " impossible de convertir le message du serveur en JSON")

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
                except socket.error:
                    pass
    def play(self,dicGame):
        #fonction qui s'occupe de renvoyé une reponse de la request move sous forme de dictionnaire
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
        if dicGame["state"]["players"][0] == self.name:
            board = dicGame["state"]["board"]
        else:
            board = [dicGame["state"]["board"][1],dicGame["state"]["board"][0]]
        if self.strat == "m":
            move = First_strategy.strat(board)
            message = "minmax"
        elif self.strat == "i":
            move, message= First_strategy.stratIterative(board)
        elif self.strat == "f":
            move = AIStrat.bestCoupInThemoment(board)
            message ="sur le coup ca me parait une bonne idee"
        elif self.strat == "n":
            move = AIStrat.strategieDuMoinsDePion(board)
            message ="le moins de pion"
        else :
            move =AIStrat.aleatoireCoup(board)
            message = "aleatoire"
        return {"response": "move","move": move,"message": message}

    #def fin(self):
        #self.run = False
        #self.threadEcoute.join() #je sais pas si c'est une bonne idée de le mettre
        # car le theads s'arrete que quand un message arrive car il est bloqué a attendre un message

#pour lance le programme depuis le terminal
#due au tread qui a pas de fin (fonction bloquante)
#_init__(self,port,name,strat ="i",matricules=['21258','20242'],servor='172.17.33.221'):
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n','--AIName',type=str, help='The name of the AI',default="Roversi")
    parser.add_argument('-p', '--port', type=int, help='The port the program use to listen for request from the serverRunner', default=8888)
    parser.add_argument('-AI', '--aiStrat', type=str, help='strategie que utilisera L\'ia (\'a\': aleatoire, \'m\'= minmax avec profondeur limité ,\'f\'= firstcoup,\'n\'=strategie du moins de coup,\'i\'= minmax avec profondeur itératif', default='i')
    parser.add_argument('-s', '--servor', type=str, help='adresse du sevrveur ChampionshipRunner', default='127.0.0.1')
    args = parser.parse_args()

    withThread=False

    AICom(port=args.port,name= args.AIName, strat=args.aiStrat, servor=args.servor)