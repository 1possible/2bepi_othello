# 2bepi_othello
matricule = [21258,20242]  
IA pour jouer à othello avec le [ChampionShipRunner](https://github.com/qlurkin/PI2CChampionshipRunner).
# Comment lancer L'IA?
## par ligne de commande
```shell
python AICom.py
```
### changer des paramètres
#### port de l'ia
le port que l'ia va utiliser pour ecoute le serveur ChampionShipRunner
```shell
python AICom.py -p 8888
```
valeur par defaut : 8888
#### nom de l'ia
```shell
python AICom.py -n Roversi
```
valeur par defaut : "Roversi"
#### la stratégie de l'ia
la stratégie que va avoir l'ia lors des parties de othello. Pour plus d'information voir la partie ci-dessous : [Stratégie utilisé](https://github.com/1possible/2bepi_othello/edit/main/README.md#strat%C3%A9gie-utilis%C3%A9) et [Autres Stratégies](https://github.com/1possible/2bepi_othello/edit/main/README.md#autre-strat%C3%A9gie).
```shell
python AICom.py -AI i
```
valeur par defaut : "i"
#### l'adresse du serveur ChampionShipRunner
```shell
python AICom.py -s 127.0.0.1
```
valeur par defaut : 127.0.0.1  
Le port du serveur ChampionShipRunner est le port 3000.
## par first.py
permet de lancer facilement plusieur AI à la fois.
Il suffit juste de retirer le # devant les AI que l'on veut connecter. 
Par defaut, il n'y a que "Roversi" activé.  
ATTENTION de ne pas lancer ia "Roversi" en même temps par first.py et par ligne de commande si les paramètre son laisser par défaut.
# Stratégie utilisé
## negamax avec profondeur variable
strat = "i"  
[Conseillé]  
Elle utilise la stratégie MinMax (negamax) en regardant le plus loin dans l'arbre possible en respectant sa contrainte de temps (Approfondissement itératif) en éliminant les branches inutile à dévlopper(Alpha Beta Pruning). Elle determine la valeur d'un coup avec la fonction heuristic.
### heuristic
la valeur que retourne heuristique dépend
* de la différence de point entre l'adversaire et le joueur
* le nombre de pion pas retournable du joueur et celui de son adversaire
* le nombre de coup possible au prochain tour du joueur et de son adversaire

# autre stratégie
## aléatoire a.k.a debilus
strat = "a"  
Il joue sans bad move, mais de facon aléaloire.

## firstcoup
strat = "f"  
Il joue le coup qui rapport le plus de pion adverse sur ce tour-ci.

## stratégie du moins de pion
strat = "n"  
Il joue le pire qui rapport le moins de point jusqu'a ce que le terrai soit rempli de moins de 50 pions sinon prend le coup qui rapport le plus de point. 
Si il y a un coup possible qui est un coin ou si il peut placer un pion imprenable par l'adversaire il les prendra en priorité.

## MinMax
strat = "m"  
Il joue en prevoyant 3 coup d'avance avec la strategie minmax en éliminant les branches inutile à dévlopper.
Il choisi sont coup en fonction de le fonction heuristic. 

# bibliothèque utilisé
* random : pour les coups aléatoires
* json et socket : pour communiquer avec le serveur
* threads : pour pouvoir lancer plusieur AI en même temps
* defaultdict from collections : pour garder en memoire les coups pour la strategie [negamax avec profondeur variable](https://github.com/1possible/2bepi_othello/edit/main/README.md#negamax-avec-profondeur-variable)
* time : pour prendre en compte le temps pour la strategie [negamax avec profondeur variable](https://github.com/1possible/2bepi_othello/edit/main/README.md#negamax-avec-profondeur-variable)
* asyncio : pour pouvoir recherche dans l'arbre tout en regardant le temps pour la strategie [negamax avec profondeur variable](https://github.com/1possible/2bepi_othello/edit/main/README.md#negamax-avec-profondeur-variable)
