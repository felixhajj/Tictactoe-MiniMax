#Version Française

#Rapport
!!note: Ce code utilise la version 3.9 de Python. Pour démarrer le projet, lancez le fichier principal et saisissez "ai" dans la console (ou "pvp" pour le mode joueur contre joueur).

Dans le code, l'algorithme minimax est utilisé pour déterminer les mouvements de l'agent IA. L'algorithme explore l'arbre, évalue chaque nœud et renvoie le score qui déterminera le meilleur mouvement en fonction de celui-ci. Le code inclut également un algorithme d'élagage alpha-bêta, utilisé pour accélérer l'algorithme minimax en réduisant le nombre de nœuds à évaluer. L'élagage alpha-bêta fonctionne en éliminant les nœuds qui sont garantis d'être pires que les nœuds déjà évalués.

Classe Board
La classe Board contient plusieurs fonctions utiles pour gérer le plateau de jeu. Le constructeur initialise un tableau numpy pour représenter le plateau vide et définit une variable pour suivre le nombre de cases marquées. La fonction final_state() vérifie les conditions de victoire sur le plateau et renvoie l'identité du joueur qui a gagné ou 0 si le jeu n'est pas encore terminé. La fonction unmark_sqr() supprime la marque d'une case donnée. La fonction get_CurrBoard() crée une nouvelle instance de Board avec le même état que la précédente. La fonction mark_sqr() marque une case donnée avec l'identité d'un joueur. La fonction empty_sqr() renvoie vrai si une case donnée est vide. La fonction get_empty_sqrs() renvoie une liste de coordonnées des cases vides sur le plateau. La fonction isfull() renvoie vrai si toutes les cases du plateau ont été marquées. La fonction isempty() renvoie vrai si aucune case n'a été marquée.

Classe Game
En utilisant Pygame, nous avons pu personnaliser notre interface en ajoutant des couleurs à notre plateau et en définissant les lignes à l'aide des fonctions : draw_fig() et show_lines().

Classe Ai
Contient l'algorithme minimax, qui est mis en œuvre en ajoutant l'élagage alpha-bêta pour améliorer les performances.








#English Version

#Report

!!note: this code is using python version 3.9. and to start the project, start the main file, and write ai in the console(or pvp for pvp)


In the code, the minimax algorithm is used to determine the AI agent's moves. The algorithm searches through the tree, evaluating each node, and returning the score, that will determine the best_move based on it.
The code also includes an alpha-beta pruning algorithm, which is used to speed up the minimax algorithm by reducing the number of nodes that need to be evaluated. Alpha-beta pruning works by eliminating nodes that are guaranteed to be worse than previously evaluated nodes.

Board class
The Board class contains several useful functions for managing the game board. The constructor initializes a numpy array to represent the empty board, and sets a variable to track the number of marked squares. 
The final_state() function checks for win conditions on the board and returns the identity of the player who won or 0 if the game is not yet finished. 
The unmark_sqr() function removes the mark from a given square. 
The get_CurrBoard() function creates a new Board instance with the same state as the current one. 
mark_sqr() function marks a given square with a player's identity. 
The empty_sqr() function returns true if a given square is empty. The get_empty_sqrs() function returns a list of coordinates of empty squares on the board.
 The isfull() function returns true if all squares on the board have been marked
the isempty() function returns true if no squares have been marked yet.

Game class
Using pygame, we were able to, personalize our interface, by putting colors to our board, and setting the lines, using the functions:
draw_fig()
show_lines()


Ai class
Contains the minimax algorithm, which is implemented and adding alpha-beta pruning to enhance the performance
