# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 10:33:24 2021

@author: equipo
"""

'''
Author: Eric P. Nichols
Date: Feb 8, 2008.
Board class.
Board data:
  1=white, -1=black, 0=empty
  first dim is column , 2nd is row:
     pieces[1][7] is the square in column 2,
     at the opposite end of the board in row 8.
Squares are stored and manipulated as (x,y) tuples.
x is the column, y is the row.
'''

import numpy as np

class Board():
        
    def __init__(self, n):
        "Set up initial board configuration."

        self.n = n
        # Create the empty board array.
        self.pieces = np.zeros((2,self.n,self.n),int)
        self.matrix_order = np.array([[1,1],[0,0],[0,1],[2,1],[2,2],[2,0],[1,0],[1,2],[0,2]])
        self.limit_number = 9

    # add [][] indexer syntax to the Board
    def __getitem__(self, index): 
        return self.pieces[index]

    def getScore(self, player):
        
        #Primer jugador
        currentPlayerPoints = 0
        
        if player == 1:
            currentPlayerMatrix = np.abs(np.reshape(self.pieces[0],self.n*self.n))
        else:
            currentPlayerMatrix = np.abs(np.reshape(self.pieces[1],self.n*self.n))
            
        #Sumas de elementos
        sumas = np.array([currentPlayerMatrix[0]+currentPlayerMatrix[1]+currentPlayerMatrix[2],
                          currentPlayerMatrix[3]+currentPlayerMatrix[4]+currentPlayerMatrix[5],
                          currentPlayerMatrix[6]+currentPlayerMatrix[7]+currentPlayerMatrix[8],
                          currentPlayerMatrix[0]+currentPlayerMatrix[3]+currentPlayerMatrix[6],
                          currentPlayerMatrix[1]+currentPlayerMatrix[4]+currentPlayerMatrix[7],
                          currentPlayerMatrix[2]+currentPlayerMatrix[5]+currentPlayerMatrix[8],
                          currentPlayerMatrix[0]+currentPlayerMatrix[4]+currentPlayerMatrix[8],
                          currentPlayerMatrix[2]+currentPlayerMatrix[4]+currentPlayerMatrix[6]])
        
        #Las sumas que incluyan un cero no cuentan
        ct = -1
        if currentPlayerMatrix[0] == 0:
            sumas[0] = ct
            ct -= 1
            sumas[3] = ct
            ct -= 1
            sumas[6] = ct
            ct -= 1
        if currentPlayerMatrix[1] == 0:
            sumas[0] = ct
            ct -= 1
            sumas[4] = ct
            ct -= 1
        if currentPlayerMatrix[2] == 0:
            sumas[0] = ct
            ct -= 1
            sumas[5] = ct
            ct -= 1
            sumas[7] = ct
            ct -= 1
        if currentPlayerMatrix[3] == 0:
            sumas[1] = ct
            ct -= 1
            sumas[3] = ct
            ct -= 1
        if currentPlayerMatrix[4] == 0:
            sumas[1] = ct
            ct -= 1
            sumas[4] = ct
            ct -= 1
            sumas[6] = ct
            ct -= 1
            sumas[7] = ct
            ct -= 1
        if currentPlayerMatrix[5] == 0:
            sumas[1] = ct
            ct -= 1
            sumas[5] = ct
            ct -= 1
        if currentPlayerMatrix[6] == 0:
            sumas[2] = ct
            ct -= 1
            sumas[3] = ct
            ct -= 1
            sumas[7] = ct
            ct -= 1
        if currentPlayerMatrix[7] == 0:
            sumas[2] = ct
            ct -= 1
            sumas[4] = ct
            ct -= 1
        if currentPlayerMatrix[8] == 0:
            sumas[2] = ct
            ct -= 1
            sumas[5] = ct
            ct -= 1
            sumas[6] = ct
            ct -= 1
        
        unique,counts = np.unique(sumas,return_counts=True)
        currentPlayerPoints += np.max(counts)-1
        """
        unique,counts = np.unique(currentPlayerMatrix,return_counts=True)
        if unique[0] == 0:
        	unique = np.delete(unique,0)
        	counts = np.delete(counts,0)
        
        if (counts>1).any():
        	currentPlayerPoints = 0
        """
        
        #Segundo jugador
               
        opponentPlayerPoints = 0
        
        if player == 1:
            opponentPlayerMatrix = np.abs(np.reshape(self.pieces[1],self.n*self.n))
        else:
            opponentPlayerMatrix = np.abs(np.reshape(self.pieces[0],self.n*self.n))

        #Sumas de elementos
        sumas = np.array([opponentPlayerMatrix[0]+opponentPlayerMatrix[1]+opponentPlayerMatrix[2],
                          opponentPlayerMatrix[3]+opponentPlayerMatrix[4]+opponentPlayerMatrix[5],
                          opponentPlayerMatrix[6]+opponentPlayerMatrix[7]+opponentPlayerMatrix[8],
                          opponentPlayerMatrix[0]+opponentPlayerMatrix[3]+opponentPlayerMatrix[6],
                          opponentPlayerMatrix[1]+opponentPlayerMatrix[4]+opponentPlayerMatrix[7],
                          opponentPlayerMatrix[2]+opponentPlayerMatrix[5]+opponentPlayerMatrix[8],
                          opponentPlayerMatrix[0]+opponentPlayerMatrix[4]+opponentPlayerMatrix[8],
                          opponentPlayerMatrix[2]+opponentPlayerMatrix[4]+opponentPlayerMatrix[6]])
        
        #Las sumas que incluyan un cero no cuentan
        ct = -1
        if opponentPlayerMatrix[0] == 0:
            sumas[0] = ct
            ct -= 1
            sumas[3] = ct
            ct -= 1
            sumas[6] = ct
            ct -= 1
        if opponentPlayerMatrix[1] == 0:
            sumas[0] = ct
            ct -= 1
            sumas[4] = ct
            ct -= 1
        if opponentPlayerMatrix[2] == 0:
            sumas[0] = ct
            ct -= 1
            sumas[5] = ct
            ct -= 1
            sumas[7] = ct
            ct -= 1
        if opponentPlayerMatrix[3] == 0:
            sumas[1] = ct
            ct -= 1
            sumas[3] = ct
            ct -= 1
        if opponentPlayerMatrix[4] == 0:
            sumas[1] = ct
            ct -= 1
            sumas[4] = ct
            ct -= 1
            sumas[6] = ct
            ct -= 1
            sumas[7] = ct
            ct -= 1
        if opponentPlayerMatrix[5] == 0:
            sumas[1] = ct
            ct -= 1
            sumas[5] = ct
            ct -= 1
        if opponentPlayerMatrix[6] == 0:
            sumas[2] = ct
            ct -= 1
            sumas[3] = ct
            ct -= 1
            sumas[7] = ct
            ct -= 1
        if opponentPlayerMatrix[7] == 0:
            sumas[2] = ct
            ct -= 1
            sumas[4] = ct
            ct -= 1
        if opponentPlayerMatrix[8] == 0:
            sumas[2] = ct
            ct -= 1
            sumas[5] = ct
            ct -= 1
            sumas[6] = ct
            ct -= 1
            
        unique,counts = np.unique(sumas,return_counts=True)
        opponentPlayerPoints += np.max(counts)-1
        """
        unique,counts = np.unique(opponentPlayerMatrix,return_counts=True)
        if unique[0] == 0:
        	unique = np.delete(unique,0)
        	counts = np.delete(counts,0)
        if (counts>1).any():
        	opponentPlayerPoints = 0
        """
        return np.array([currentPlayerPoints, opponentPlayerPoints])

    def get_legal_moves(self, player):
        """Returns all the legal moves for the given color.
        (1 for white, -1 for black
        """
        
        return 1

    def has_legal_moves(self):
        if np.count_nonzero(self.pieces) < self.n*self.n*2:
            return True
        return False
    
    def execute_move(self, move, player):
        
        if player == 1:
            current_moves = np.count_nonzero(np.abs(self.pieces[0]))
        else:
            current_moves = np.count_nonzero(np.abs(self.pieces[1]))
            
        if current_moves > 8:
            current_moves = 8
        
        next_move_index = self.matrix_order[current_moves]
        
        if player == 1:
            self.pieces[0][next_move_index[0]][next_move_index[1]] = move+1
        else:
            self.pieces[1][next_move_index[0]][next_move_index[1]] = -move-1
            
        #print("\n------------------------\n" + str(self.pieces) + "\nLegal moves: " + str(self.has_legal_moves()) + "\nMove: " + str(move) + "\nNMI: " + str(next_move_index) + "\nCurrent moves: " + str(current_moves) + "\nPlayer: " + str(player) + "\n------------------------\n")
        
                
        
