# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 13:12:29 2021

@author: equipo
"""

import numpy as np
import logging

class Game: #Clase general del juego

    def __init__(self):		#Valores de inicio
        self.currentPlayer = 1  #Empieza el jugador 1
        self.limit_number = 113
        self.gameState = GameState(np.zeros(self.limit_number*2, dtype=np.int), 1) #Inicia un estado de juego. Tablero unidimensional vacío. Empieza el jugador 1
        self.actionSpace = np.zeros(self.limit_number*2, dtype=np.int) #??
        self.pieces = {'9':'I','8':'H','7':'G','6':'F','5':'E','4':'D','3':'C','2':'B','1':'A','0':'-','-1':'R','-2':'S','-3':'T','-4':'U','-5':'V','-6':'W','-7':'X','-8':'Y','-9':'Z'}
        self.grid_shape = (1,self.limit_number*2) #Forma del tablero ¿?
        self.input_shape = (2,1,self.limit_number*2) #??
        self.name = 'matrices' #Nombre del juego
        self.state_size = len(self.gameState.binary) #??
        self.action_size = len(self.actionSpace) #??
        
    def reset(self): #Resetea el juego: vacia el tablero y vuelve a empezar el jugador 1
        self.gameState = GameState(np.zeros(self.limit_number*2, dtype=np.int), 1)
        self.currentPlayer = 1
        return self.gameState
    
    def step(self, action): #Realiza un movimiento en el juego
        next_state, value, done = self.gameState.takeAction(action) #Coloca la el numero en la casilla correspondiente con la función takeAction del GameState
        self.gameState = next_state #Actualiza el estado del juego
        self.currentPlayer = -self.currentPlayer #Cambia el jugador (de 1 a -1 o de -1 a 1)
        info = None #??
        return ((next_state, value, done, info))  #Devuelve el nuevo estado del juego, si la partida ha terminado o no y los puntos de cada jugador en tal caso.

    def identities(self, state, actionValues):#Esta función sirve para "Data augmentation" o Aumento de datos que es, básicamente, introducir en la memoria la misma partida con el tablero invertido varias veces para que la red neuronal tenga más datos con los que aprender.
        identities = [(state,actionValues)]
        return identities
    

class GameState(): #Clase que define el estado del juego
    def __init__(self, board, playerTurn):
        self.board = board #Situación del tablero actual del juego
        self.limit_number = len(self.board)//2
        self.matrix_order = np.array([2,3,9,7,1,8,6,4,5]) #Orden en el que colocamos los elementos de la matriz
        self.pieces = {'9':'I','8':'H','7':'G','6':'F','5':'E','4':'D','3':'C','2':'B','1':'A','0':'-','-1':'R','-2':'S','-3':'T','-4':'U','-5':'V','-6':'W','-7':'X','-8':'Y','-9':'Z'}
        self.winners = []
        self.playerTurn = playerTurn #A qué jugador le toca mover
        self.binary = self._binary() #?? Crea un array con el doble del tamaño del tablero: Un tablero solo con las posiciones del primer jugador y otro solo con las del segundo jugador. Creo que sirve para algo de la red neuronal pero no lo tengo claro.
        self.id = self._convertStateToId() #?? Igual que binary pero lo convierte en texto. No sé para qué sirve.
        self.allowedActions = self._allowedActions() #Acciones permitidas según las reglas del juego
        self.isEndGame = self._checkForEndGame() #Comprueba si el juego ha terminado
        self.value = self._getValue() #Comprueba quien ha ganado y cuantos puntos tiene cada uno
        self.score = self._getScore() #Puntuacion de cada jugador
    
    def _allowedActions(self): #Se permite mover ficha en cualquier posicion siempre que tenga el valor 0 (es decir, que este vacia) dentro del tablero del jugador
                
        if self.playerTurn == 1:
            allowed = np.array(np.where(self.board[0:self.limit_number]==0)[0])
        else:
            allowed = np.array(np.where(self.board[self.limit_number:2*self.limit_number]==0)[0]+self.limit_number)

        return allowed
    
    def _binary(self): #Devuelve un array con el tablero repetido dos veces: Una primera vez en la que las casillas ocupadas por el jugador 1 valen 1 y el resto cero y una segunda vez en la que las casillas ocupadas por el otro jugador valen 1 y el resto cero.
        
        currentplayer_position = np.zeros(self.limit_number*2, dtype=np.int)
        currentplayer_position[np.where(self.board*self.playerTurn > 0)] = 1
        
        other_position = np.zeros(self.limit_number*2, dtype=np.int)
        other_position[np.where(self.board*self.playerTurn < 0)] = 1
            
        position = np.append(currentplayer_position,other_position)

        return (position)
    
    def _convertStateToId(self): #Igual que binary pero lo convierte a texto (string)
        player1_position = np.zeros(self.limit_number*2, dtype=np.int)
        player1_position[np.where(self.board>0)] = 1
        
        other_position = np.zeros(self.limit_number*2, dtype=np.int)
        other_position[np.where(self.board<0)] = 1

        position = np.append(player1_position,other_position)

        id = ''.join(map(str,position))

        return id
    
    def _checkForEndGame(self): #Comprueba si ha terminado la partida. En este caso termina cuando todas las casillas están ocupadas
        if np.count_nonzero(self.board) == 18:
            return 1
        return 0
    
    def _getValue(self): #Cuenta los puntos de la partida y decide quién ha ganado
        #Primer jugador
        currentPlayerPoints = 0
        
        #Traducimos el tablero en matriz
        currentPlayerMatrix = np.zeros(9,dtype=np.int)
        if self.playerTurn == 1:
            for i in range(9):
                if len(np.where(self.board[0:self.limit_number]==self.matrix_order[i])[0])>0:
                    currentPlayerMatrix[i] = np.where(self.board[0:self.limit_number]==self.matrix_order[i])[0][0]+1
        else:
            for i in range(9):
                if len(np.where(self.board[self.limit_number:self.limit_number*2]==-self.matrix_order[i])[0])>0:
                    currentPlayerMatrix[i] = np.where(self.board[self.limit_number:self.limit_number*2]==-self.matrix_order[i])[0][0]+1

       #Reglas formales        
        currentPlayerPointsFor = 0        
        
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
        maximo = np.max(counts)
        if maximo > 1:
            currentPlayerPointsFor += maximo-1
            
        currentPlayerPoints=currentPlayerPointsFor
        
        #Segundo jugador
               
        opponentPlayerPoints = 0
        
        #Traducimos el tablero en matriz
        opponentPlayerMatrix = np.zeros(9,dtype=np.int)
        if self.playerTurn == -1:
            for i in range(9):
                if len(np.where(self.board[0:self.limit_number]==self.matrix_order[i])[0])>0:
                    opponentPlayerMatrix[i] = np.where(self.board[0:self.limit_number]==self.matrix_order[i])[0][0]+1
        else:
            for i in range(9):
                if len(np.where(self.board[self.limit_number:self.limit_number*2]==-self.matrix_order[i])[0])>0:
                    opponentPlayerMatrix[i] = np.where(self.board[self.limit_number:self.limit_number*2]==-self.matrix_order[i])[0][0]+1


        #Reglas materiales 
        
        #Reglas formales
        opponentPlayerPointsFor = 0
        
        
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
        maximo = np.max(counts)
        if maximo > 1:
            opponentPlayerPointsFor += maximo-1

        opponentPlayerPoints=opponentPlayerPointsFor
        
        
        if currentPlayerPoints > opponentPlayerPoints:
            return (1, currentPlayerPoints, opponentPlayerPoints)
        elif currentPlayerPoints < opponentPlayerPoints:
            return (-1, currentPlayerPoints, opponentPlayerPoints)
        else:
        	return (0, currentPlayerPoints, opponentPlayerPoints)
        
    def _getScore(self): #Puntuacion de la partida. La obtiene de self.value
        tmp = self.value
        return (tmp[1], tmp[2])
        
    def takeAction(self, action): #Coloca la ficha en el tablero y comprueba si ha terminado la partida
        newBoard = np.array(self.board)
        
        if self.playerTurn == 1:
            position = np.count_nonzero(newBoard[0:self.limit_number])+1
            newBoard[action] = position
        else:
            position = np.count_nonzero(newBoard[self.limit_number:self.limit_number*2])+1
            newBoard[action] = -position
            
        newState = GameState(newBoard, -self.playerTurn)
        
        value = 0
        done = 0
        
        if newState.isEndGame:
            value = newState.value[0]
            done = 1
        
        return (newState, value, done)  #Devuelve el nuevo estado del juego, si la partida ha terminado o no y los valores del juego (ganador y puntuaciones)
    
    def render(self, logger): #Esta funcion sirve para almacenar la evolucion de la partida y permitir que sea visualizada guardándola en un archivo
        tmp = self.value
        
        mat1 = np.zeros(9,dtype=np.int)
        for i in range(9):
            if len(np.where(self.board[0:self.limit_number]==self.matrix_order[i])[0])>0:
                mat1[i] = np.where(self.board[0:self.limit_number]==self.matrix_order[i])[0][0]+1
        
        logger.info('Matriz 1')
        for r in range(3):
            logger.info([str(mat1[x]) for x in range(3*r,3*r+3)])
        if self.playerTurn == 1:
            logger.info("Score 1: " + str(tmp[1]))
        else:
            logger.info("Score 1: " + str(tmp[2]))

        mat2 = np.zeros(9,dtype=np.int)
        for i in range(9):
            if len(np.where(self.board[self.limit_number:self.limit_number*2]==-self.matrix_order[i])[0])>0:
                mat2[i] = np.where(self.board[self.limit_number:self.limit_number*2]==-self.matrix_order[i])[0][0]+1
        
        logger.info('Matriz 2')
        for r in range(3):
            logger.info([str(mat2[x]) for x in range(3*r,3*r+3)])
        if self.playerTurn == 1:
            logger.info("Score 2: " + str(tmp[2]))
        else:
            logger.info("Score 2: " + str(tmp[1]))
        logger.info('--------------')
        


