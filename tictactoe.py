import sys
import pygame
import numpy as np

from constants import *
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE AI')
screen.fill(BG_COLOR)

class Board:

    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))
        self.empty_sqrs = self.squares # [squares]
        self.marked_sqrs = 0

    def final_state(self, mmboard):
        '''
        @return 1.5 if there is no win yet
        @return 1 if player 1 wins
        @return 2 if player 2 wins
        '''

        for col in range(COLS):
            if self.squares[0][col]== self.squares[1][col] == self.squares[2][col] !=0:
                return self.squares[0][col] #just return any of the 3 because they carry the identity of the player who won(1 or 2)

        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                return self.squares[row][0]

        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            return self.squares[0][0]
        if self.squares[0][2] == self.squares[1][1] == self.squares[2][0] != 0:
            return self.squares[0][2]

        if len(mmboard.get_empty_sqrs()) > 0:
            return 0
        else:
            return 1.5


    def unmark_sqr(self, x, y):
        self.squares[x][y] = 0

    def get_CurrBoard(self):
        board = Board()
        board.squares = self.squares.copy()

        return board

    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1

    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0
    def get_empty_sqrs(self):
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_sqr(row, col):
                    empty_sqrs.append((row, col))
        return empty_sqrs
    def isfull(self):
        return self.marked_sqrs == 9
    def isempty(self):
        return self.marked_sqrs == 0

class AI:
    def __init__(self):
        pass
#3eyiz l class la eza badde hott gher algorithm gher el minimax bas enno me7en
    def minimax(self, mmboard, player, alpha, beta):  # no need to pass the player, but i did anyways //// mmboard is the current state of the game
        emptysqrs = mmboard.get_empty_sqrs()

        if player == 2:  # maximizing player's turn(player 1 is us and 2 is the computer)
            best_score = float('-inf')
            best_move = None  # in the minimax, we only need to update the best_move variable in the max section
            for x, y in emptysqrs:
                mmboard.mark_sqr(x, y, player)
                if mmboard.final_state(mmboard) == 0 and (alpha < beta):  # cause if alpha>=beta, minimize will never choose the branch # there are still empty squares left
                    score, _ = self.minimax(mmboard, (player % 2 + 1), alpha, beta)
                else:
                    score = mmboard.final_state(mmboard)

                if score > best_score:
                    best_score = score
                    alpha = best_score
                    best_move = (x, y)

                mmboard.unmark_sqr(x, y)

                if alpha >= beta:
                    break

            return best_score, best_move

        else:  # minimizing player's turn
            worst_score = float('inf')  # here, we are trying to minimize the best score
            best_move = None

            for x, y in emptysqrs:
                mmboard.mark_sqr(x, y, player)
                if mmboard.final_state(mmboard) == 0 and (beta > alpha):  # cause if beta <= alpha, maximize will never choose the branch # there are still empty squares left
                    score, _ = self.minimax(mmboard, (player % 2 + 1), alpha, beta)
                    worst_score = min(worst_score, score)  # choose the lowest between the best_score and the score
                    #mmboard.unmark_sqr(x, y)
                else:
                    score = mmboard.final_state(mmboard)

                worst_score = min(worst_score, score)
                beta = worst_score
                mmboard.unmark_sqr(x, y)

                if beta <= alpha:
                    break

            return worst_score, best_move


class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.player = 1 #1-cross #2-circles
        #self.gamemode = 'ai' #pvp or ai
        self.running = True # if gameover or not
        self.show_lines()
        self.show_lines()
    def show_lines(self):
        #vertical
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - SQSIZE, 0), (WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)

        #horizontal
        pygame.draw.line(screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT-SQSIZE), (WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)


    def draw_fig(self, row, col):
        if self.player == 1:
            #draw cross
            #desc line
            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
            #asc line
            start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            end_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)
        elif self.player==2:
            #draw circle
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE+SQSIZE // 2)
            pygame.draw.circle(screen, CIRC_COLOR, center, RADIUS, CIRC_WIDTH)

    def next_turn(self):
        self.player = self.player % 2 +1


def click(event, game):
    if event.type == pygame.MOUSEBUTTONDOWN:
        mousex, mousey = pygame.mouse.get_pos()
        col = mousex // SQSIZE
        row = mousey // SQSIZE

        if game.board.empty_sqr(row, col):
            game.board.mark_sqr(row, col, game.player)
            game.draw_fig(row, col)
            #game.board.unmark_sqr(row,col)

            winner = game.board.final_state(game.board.get_CurrBoard())
            if winner != 0 and winner != 1.5:
                game.running = False
                print(f"Player {winner} wins!")
            else:

                game.player = game.player % 2 + 1

    return game.running
def main():
    game = Game()
    gamemode = input("enter gamemode(ai or pvp): ")

    while game.running:
        for event in pygame.event.get():
            currboard = game.board.get_CurrBoard()
            if event.type == pygame.QUIT:
                game.running = False
                sys.exit()
            if game.player == 1:
                   if click(event, game):
                       break

            if game.player == 2:
                if gamemode == 'pvp':
                    if click(event, game):
                        break

                elif gamemode == 'ai':
                    row, col = game.ai.minimax(game.board.get_CurrBoard(), game.player, float('-inf'), float('inf'))[1]

                    #print(row, " ", col)
                    game.board.mark_sqr(row, col, game.player)
                    game.draw_fig(row, col)

                    winner = game.board.final_state(currboard)
                    if winner != 1.5 and winner != 0:
                        game.running = False
                        print(f"Player {winner} wins!")

                    game.player = game.player % 2 + 1

        if game.board.isfull():
            game.running = False
            if game.board.final_state(game.board.get_CurrBoard()) == 1.5:
                print("Draw!")
            break

        pygame.display.update()


#!!
main()
