import unittest
from ddt import ddt,data,unpack
from uuid import UUID
from copy import deepcopy
from User import *

@ddt
class TestUserGet(unittest.TestCase):

    @data("Timmy","Tammy","Tommy")
    def test_user_getname(self,want):
        user1 = User(want)
        self.assertTrue(user1.getName()==want)
    
    @data("Timmy","Tammy","Tommy")    
    def test_user_getid(self,want):
        user1 = User(want)
        self.assertTrue(UUID(user1.getId(),version=4))
        
    @data("Timmy","Tammy","Tommy")    
    def test_user_equality(self,want):
        user1 = User(want)
        user2 = deepcopy(user1)
        self.assertTrue(user1==user2)
        
        
if __name__ == '__main__':
    unittest.main()