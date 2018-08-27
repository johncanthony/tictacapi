from redisco import models
from uuid import uuid4
import jsonstr
import json

SLICES={
        'VERTICAL':[[0,0],[0,0],[0,0]],
        'HORIZONTAL':[[0,0],[0,0],[0,0]],
        'DIAGONAL':[[0,0],[0,0]]
       }
         



class Board(models.Model):
    
    uid = models.Attribute(default=str(uuid4()))
    slices = models.Attribute(default=json.dumps(SLICES))
    available_moves = models.ListField(int,default=[0,0,0,0,0,0,0,0,0])
    

    
    
class BoardController():

    SLICES_CONST_MAP={1:'VERTICAL',2:'HORIZONTAL',3:'DIAGONAL'}

    MOVE_TRANSLATION={1:[0,0,[0]],
                      2:[0,1,[]],
                      3:[0,2,[1]],
                      4:[1,0,[]],
                      5:[1,1,[0,1]],
                      6:[1,2,[]],
                      7:[2,0,[1]],
                      8:[2,1,[]],
                      9:[2,2,[0]] }
 
    def __init__(self,Board_obj):
        
        self.board = Board_obj
        self.Slices = jsonstr.loads(self.board.slices)

    def getVerticals(self):
        return self.Slices[Board.SLICES_CONST_MAP[1]] 

    def getHorizontals(self):
        return self.Slices[Board.SLICES_CONST_MAP[2]]
        
    def getDiagonals(self):
        return self.Slices[Board.SLICES_CONST_MAP[3]]
    
    def getAvailable_moves(self):
        rlist=[]
        for index in range(len(self.board.available_moves)):
            if(self.board.available_moves[index]==0):
                rlist.append(index+1)
        
        return rlist
    
    
    def updateAvailable_moves(self,move_index):
        if(self.board.available_moves[move_index-1] != 0):
            return False
        

        
        self.board.available_moves[move_index-1] = 1
        
        self.board.update_attributes(available_moves=self.board.available_moves)
        self.board.save()

        return True
    
    
    def setSlice(self,mode,uid,index):
        bslice=self.Slices[mode][index]
        
        if(bslice[0]==-1):
            return
        
        if(bslice[0]==0):
            bslice[0]=uid
            bslice[1]=1
            return
        
        if(bslice[0]!=0):
            if(bslice[0]==uid):
                bslice[1]+=1
            if(bslice[0]!=uid):
                self.Slices[mode][index]=[-1,-1]
    
                
    def checkWin(self):
        
        for slice_mode in self.Slices.keys():
            for slice_index in self.Slices[slice_mode]:
                if slice_index[1] == 3:
                    return slice_index[0]
        
        return 0

    def setPiece(self,player_uid,space):
        #Check the move is available
        if(not self.updateAvailable_moves(space)):
            return False
            
        slice_Changes=self.MOVE_TRANSLATION[space]
        #set horizontal
        self.setSlice(self.SLICES_CONST_MAP[2],player_uid,slice_Changes[0])
        #set vertical
        self.setSlice(self.SLICES_CONST_MAP[1],player_uid,slice_Changes[1])
        #set diagonals
        for each in slice_Changes[2]:
            self.setSlice(self.SLICES_CONST_MAP[3],player_uid,each)
   
        self.board.update_attributes(slices=json.dumps(self.Slices))
        self.board.save()

        return True
        
    def getBoardDict(self):
        return {"uid":self.board.uid,"availableMoves":self.board.availableMoves,"slices":self.board.Slices}
                
