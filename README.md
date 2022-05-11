# 2bepi_othello
matricule = [21258,20242]
# Stratégie utilisé
## negamax avec profondeur variable
strat = "i"  
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
* random : pour les coup aléatoire
* json et socket : pour communiquer avec le serveur
* threads : pour pouvoir lancer plusieur AI en même temps
* defaultdict from collections : pour garder en memoire les coups pour la strategie "negamax a profondeur variable"
* time : pour prendre en compte le temps pour la strategie "negamax a profondeur variable"
* asyncio : pour pouvoir recherche dans l'arbre tout en regardant le temps pour la "strategie negamax a profondeur variable"
