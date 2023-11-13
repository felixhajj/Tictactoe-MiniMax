# Report

In the code, the minimax algorithm is used to determine the AI agent's moves. The algorithm searches through the tree, evaluating each node, and returning the score, that will determine the best_move based on it.
The code also includes an alpha-beta pruning algorithm, which is used to speed up the minimax algorithm by reducing the number of nodes that need to be evaluated. Alpha-beta pruning works by eliminating nodes that are guaranteed to be worse than previously evaluated nodes.
#Board class
The Board class contains several useful functions for managing the game board. The constructor initializes a numpy array to represent the empty board, and sets a variable to track the number of marked squares. 
The final_state() function checks for win conditions on the board and returns the identity of the player who won or 0 if the game is not yet finished. 
The unmark_sqr() function removes the mark from a given square. 
The get_CurrBoard() function creates a new Board instance with the same state as the current one. 
mark_sqr() function marks a given square with a player's identity. 
The empty_sqr() function returns true if a given square is empty. The get_empty_sqrs() function returns a list of coordinates of empty squares on the board.
 The isfull() function returns true if all squares on the board have been marked
the isempty() function returns true if no squares have been marked yet.
#Game class
Using pygame, we were able to, personalize our interface, by putting colors to our board, and setting the lines, using the functions:
draw_fig()
show_lines()

#Ai class
Contains the minimax algorithm, which is implemented and adding alpha-beta pruning to enhance the performance
