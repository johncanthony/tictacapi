from uuid import uuid4
from User import *
from Board import *

#TODO refactor to handle CAT
class Game:
    #TODO create user population from dictionary
    def __init__(self, game=None):
        if(game!=None):
            self.uid=game['uid']
            self.state=game['state']
            self.users=[]
            #pull each user dict from the game dict and append it to the object user list
            for each_user in game['users']:
               temp_User=User(each_user['name'],each_user['uid']) 
               self.users.append(temp_User)
            self.board=game['board']
            return
        
        self.uid = str(uuid.uuid4())
        self.state= 0
        self.users=[-1,-1]
        self.board = Board()
        
    def __str__(self):
        return str(self.getGameDict())
        
    def getId(self):
        return self.uid
        
    def getState(self):
        return self.state
        
    def getUser(self,index):
        return(self.users[index-1])
    
    def setUser(self,player_name,number):
        player_user=User(player_name)
        self.users[number-1] = player_user
        if(-1 not in self.users):
            self.state=1
    
    #this should probably run a try catch for the setPiece and enable the set piece to throw and exception if an invalid move is made
    def move(self,board_index):
        if(not self.board.setPiece(self.users[self.state-1].getId(),board_index)):
            return "invalid"
        
        #Make move and check for CAT
        if(not self.board.checkWin() and (len(self.board.getAvailable_moves())<1)):
            self.state=4
            return "CAT"
        
        if(self.board.checkWin()):
            winner=self.users[self.state-1]
            self.state=3
            return winner
        
        if(self.state==1):
            self.state=2
        elif(self.state==2):
            self.state=1
        
        return False
                
        
       
        
        
    
    def getGameDict(self):
        return({
            'uid':self.uid,
            'state':self.state,
            'users':[self.users[0].getUserDict(),self.users[1].getUserDict()],
            'board': self.board.getBoardDict()
            
        })
        
        
        