from uuid import uuid4
from User import *
from Board import *

from redisco import models


class Game(models.Model):


    uid = models.Attribute(default=str(uuid4()))
    state = models.IntegerField(default=0)
    
    player1 = models.Attribute(default="-1")
    player2 = models.Attribute(default="-1")

    board = models.ReferenceField(Board)
    
    
class GameController():

    def __init__(self, game):
        self.game = game


    #def setUser(self,player,number):
    #    self.game.users[number-1] = player
    #    if("-1" not in self.game.users):
    #        self.game.state=1
    #
    #
    #    self.game.save()
    
    def setUser(self,player):
        
        if(self.game.player1 == "-1"):
            self.game.player1 = player
        elif (self.game.player2 == "-1"):
            self.game.player2 = player
            self.game.state = 1

        self.game.save()
   

    def move(self,board_index):

        
        board_controller = BoardController(self.game.board)

        if(self.game.state==1):
            cur_player = self.game.player1
            self.game.state=2
        elif(self.game.state==2):
            cur_player = self.game.player2
            self.game.state=1


        if(not board_controller.setPiece(cur_player,board_index)):
            return "invalid"

        #Make move and check for CAT
        if(not board_controller.checkWin() and (len(board_controller.getAvailable_moves())<1)):
            self.game.state=4
            self.game.save()
            return "CAT"

        if(board_controller.checkWin()):
            self.game.state=3
            self.game.save()
            return cur_player

        
        self.game.save()

        return False


            
        
