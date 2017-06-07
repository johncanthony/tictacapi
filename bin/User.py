import uuid


class User():
    
    
    def __init__(self,name):
        self.name = name
        self.uid = str(uuid.uuid4())
        
        
    def __eq__(self,other):
        
        if(not isinstance(other,User)):
            return False
        
        if(self.getId() != other.getId()):
            return False
            
        if(self.getName() != other.getName()):
            return False
            
        return True
        
    def getName(self):
        return self.name
    
    def getId(self):
        return self.uid
        
    def getUserDict(self):
        return {"name":self.name,"uid":self.uid} 