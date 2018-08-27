from redisco import models
from uuid import uuid4

class User(models.Model):
    
    name = models.Attribute()
    uid = models.Attribute()
    passwd = models.Attribute()



    
