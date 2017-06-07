import unittest
from ddt import ddt,data,unpack
from uuid import UUID
from Game import *
from User import *

@ddt
class TestUserGet(unittest.TestCase):
    
    
    def test_game_getid(self):
        Game1 = Game()
        self.assertTrue(UUID(Game1.getId(),version=4))
    
    @data((1,"Jim"),(2,"Jill"))
    @unpack
    def test_set_User(self,number,name):
        game = Game()
        game.setUser(name,number)
        
        self.assertTrue(game.getUser(number).getName()==name)

    @data((1,"Jim",2,"Jill"))
    def test_state_after_two_players_added(self,have):
        game=Game()
        game.setUser(have[1],have[0])
        game.setUser(have[3],have[2])
        
        self.assertTrue(game.getState()==1)
        

    def test_get_State(self):
        game = Game()
        self.assertTrue(game.getState()==0)
        
    @data({"player1":"john","player2":"maire",'moves':[1,1,1,1,5,2,4,3]})
    def test_game_move_winner(self,have):
        game=Game()
        game.setUser(have['player1'],1)
        game.setUser(have['player2'],2)
        
        for move in have['moves']:
            winner=game.move(move)
        
        print(game)
        self.assertTrue(winner.getName()==have["player1"])
        
    
        
    
if __name__ == '__main__':
    unittest.main()