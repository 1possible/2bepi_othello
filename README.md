# 2bepi_othello
# Stratégie utilisé
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
Il joue en prevoyant 2 coup d'avance avec la strategie minmax en éliminant les branches unitil à dévlopper.
Il choisi sont coup en fonction de le fonction heuristic. 
### heuristic
la valeur que retourne heuristique dépend
* de la différence de point entre l'adversaire et le joueur
* le nombre de pion inretournable du joueur

# bibliothèque utilisé
* random : pour les coup aléatoire
* json et socket : pour communiquer avec le serveur
* threads : pour pouvoir lancer plusieur AI en même temps
