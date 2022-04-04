# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 10:31:07 2021

@author: equipo
"""


from __future__ import print_function
import sys
sys.path.append('..')
from Game import Game
from .MatricesLogic import Board
import numpy as np
import logging

class MatricesGame(Game):
    square_content = {}
    

    @staticmethod
    def getSquarePiece(piece):
        return MatricesGame.square_content[piece]

    def __init__(self, n, board_length=3):
        self.n = board_length
        self.limit_number = 9

    def getInitBoard(self):
        # return initial board (numpy board)
        b = Board(self.n)
        return np.array(b.pieces)

    def getBoardSize(self):
        return (2, self.n, self.n)

    def getActionSize(self):
        # return number of actions
        return self.limit_number

    def getNextState(self, board, player, action):
        # if player takes action on board, return next (board,player)
        # action must be a valid move
        b = Board(self.n)
        b.pieces = np.copy(board)
        move = action
        b.execute_move(move, player)
        return (b.pieces, -player)

    def getValidMoves(self, board, player):
        # return a fixed size binary vector
        """
        b = Board(self.n)
        b.pieces = np.copy(board)
        legal_moves =  b.get_legal_moves(player)
        valids = np.zeros(self.limit_number,int)
        if len(legal_moves>0):
            valids[legal_moves] = 1
        """  
        valids = np.ones(self.limit_number)
        return valids

    def getGameEnded(self, board, player):
        # return 0 if not ended, 1 if this player won, -1 if this player lost
        b = Board(self.n)
        b.pieces = np.copy(board)
        #print("\n------------------------\n" + str(b.pieces) + "\n" + str(b.has_legal_moves()) + "\n------------------------\n")
        if b.has_legal_moves() == False:
            tmp = b.getScore(player)
            """
            print("--------------------")
            print(b.pieces[0])
            if player == 1:
                print("Score 1: " + str(tmp[0]))
            else:
                print("Score 1: " + str(tmp[1]))
            
            print("\n")
            print(b.pieces[1])
            if player == 1:
                print("Score 2: " + str(tmp[1]))
            else:
                print("Score 2: " + str(tmp[0]))            
            """  
            if tmp[0]>tmp[1]:
                #print("Gana este")
                return 1
            elif tmp[0]<tmp[1]:
                #print("Gana el otro")
                return -1
            else:
                #print("Empate")
                return 0.001
            
        return 0

    def getCanonicalForm(self, board, player):
        # return state if player==1, else return -state if player==-1
        if player == -1:
        	tmpboard = np.copy(board)
        	board[0] = np.copy(tmpboard[1])
        	board[1] = np.copy(tmpboard[0])
        return player*board

    #¿Se podría hacer alguna simetria?
    def getSymmetries(self, board, pi):
        return [(board,pi)]
    
    def stringRepresentation(self, board):
        return board.tostring()

    def stringRepresentationReadable(self, board):
        board_s = "".join(str(self.board[square]) for row in board for square in row)
        return board_s

    def getScore(self, board, player):
        b = Board(self.n)
        b.pieces = np.copy(board)
        return b.getScore(player)[0]


    @staticmethod
    def display(board):
        n = board.shape[1]
        
        b = Board(n)
        b.pieces = np.copy(board)
        
        print("-----------------------")
        print("Matriz 1")
        print("   ", end="")
        for y in range(n):
            print(y, end=" ")
        print("")
        for y in range(n):
            print(y, "|", end="")    # print the row #
            for x in range(n):
                piece = board[0][y][x]    # get the piece to print
                print(piece, end=" ")
            print("|")
            
        print("Score 1 =", end=" ")
        print(b.getScore(1)[0])

        print("-----------------------")
        print("Matriz 2")
        print("   ", end="")
        for y in range(n):
            print(y, end=" ")
        print("")
        for y in range(n):
            print(y, "|", end="")    # print the row #
            for x in range(n):
                piece = board[1][y][x]    # get the piece to print
                print(piece, end=" ")
            print("|")
            
        print("Score 2 =", end=" ")
        print(b.getScore(-1)[0])

        print("-----------------------")
        
        

    def render(self, board, logger):
        b = Board(self.n)
        b.pieces = np.copy(board)
        
        logger.info("-----------------------")
        logger.info("Matriz 1")
        for x in range(self.n):            
            logger.info([str(np.abs(board[0][x][y])) for y in range(0,3)])
            
        logger.info("Score 1: " + str(b.getScore(1)[0]))

        logger.info("Matriz 2")
        
        for x in range(self.n):
            logger.info([str(np.abs(board[1][x][y])) for y in range(0,3)])
            
        logger.info("Score 2 : " + str(b.getScore(-1)[0]))
        logger.info("-----------------------")

