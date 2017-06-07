from uuid import uuid4

class Board():
    
    SLICES_CONST_MAP={1:'VERTICAL',2:'HORIZONTAL',3:'DIAGONAL'}
    MOVE_TRANSLATION={1:[0,0,[0]],
                      2:[0,1,[]],
                      3:[0,2,[1]],
                      4:[1,0,[]],
                      5:[1,1,[0,1]],
                      6:[1,2,[]],
                      7:[2,0,[0]],
                      8:[2,1,[]],
                      9:[2,2,[0,1]] }
    
    def __init__(self,board=None):
        if(board!=None):
            self.uid=board['uid']
            self.Slices=board['slices']
            self.availableMoves=board['availableMoves']
            return
            
        self.uid=str(uuid4())
        self.availableMoves=[0,0,0,0,0,0,0,0,0]
        
        #Slices represent the three vertical[1] and horizontal[2] col/rows on the board and the two diagonals[3]       
        self.Slices={
                        'VERTICAL':[[0,0],[0,0],[0,0]],
                        'HORIZONTAL':[[0,0],[0,0],[0,0]],
                        'DIAGONAL':[[0,0],[0,0]]
                    }
                    
    def __str__(self):
        return str(self.getBoardDict())
    
    
    def getId(self):
        return self.uid
        
    def getVerticals(self):
        return self.Slices[Board.SLICES_CONST_MAP[1]]
    
    def getHorizontals(self):
        return self.Slices[Board.SLICES_CONST_MAP[2]]
        
    def getDiagonals(self):
        return self.Slices[Board.SLICES_CONST_MAP[3]]
    
    def getAvailable_moves(self):
        rlist=[]
        for index in range(len(self.availableMoves)):
            if(self.availableMoves[index]==0):
                rlist.append(index+1)
        
        return rlist
    
    
    def updateAvailable_moves(self,move_index):
        if(self.availableMoves[move_index-1] != 0):
            return False
        
        self.availableMoves[move_index-1] = 1
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
    
        return True
        
    def getBoardDict(self):
        return {"uid":self.uid,"availableMoves":self.availableMoves,"slices":self.Slices}
                
