import unittest
from ddt import ddt,data,unpack,file_data
from uuid import UUID,uuid4
from Board import *

@ddt
class TestBoard(unittest.TestCase):

    #Tests for a valid uuid4 set in the object
    def test_board_getId(self):
        board1 = Board()
        self.assertTrue(UUID(str(board1.getId()),version=4))
     
    
    @data([1,2,3,4,5,6,7,8,9])
    def test_board_getAvailable_moves(self,want):
        board1 = Board()
        self.assertTrue(board1.getAvailable_moves() == want)
        
    @data([[0,0],[0,0],[0,0]])
    def test_board_getVertical(self,want):
        board1 = Board()
        self.assertTrue(board1.getVerticals()==want)
        
    @data([[0,0],[0,0],[0,0]])
    def test_board_getHorizontal(self,want):
        board1 = Board()
        self.assertTrue(board1.getHorizontals()==want)
    
    @data([[0,0],[0,0]])
    def test_board_getDiagonal(self,want):
        board1 = Board()
        self.assertTrue(board1.getDiagonals()==want)
        
        
        
    @data([1],
          (1,2),
          (1,6),
          (1,2,5,3),
          (1,2,3,9,7))
    def test_board_updateAvailable_moves(self,moves):
        board1 = Board()
        for index in range(len(moves)):
            self.assertTrue(board1.updateAvailable_moves(moves[index]))
    
    
    
    #This tests to see if the vertical index will be
    #updated by the setVertical function appropriately with a given list of indexes and UUIDs. 
    @file_data('setSlice_test.json')
    #@unpack
    def test_board_setSlice_Vertical(self,test_entry):
        board1 = Board()
        have=test_entry[0]
        want=test_entry[1]
        for index in range(len(have)):
            board1.setSlice('VERTICAL',have[index][0],have[index][1])
            self.assertTrue(board1.getVerticals()==want[index])
    
    
    #This tests to see if the vertical index will be
    #updated by the setHorizontal function appropriately with a given list of indexes and UUIDs. 
    @file_data('setSlice_test.json')
    #@unpack
    def test_board_setSlice_Horizontal(self,test_entry):
        board1 = Board()
        have=test_entry[0]
        want=test_entry[1]
        for index in range(len(have)):
            board1.setSlice('HORIZONTAL',have[index][0],have[index][1])
            self.assertTrue(board1.getHorizontals()==want[index])
    
    #This tests to see if the checkWin returns the correct value after submitting a set of moves to the board
    @file_data('checkWin_test.json')
    def test_board_checkWin(self,test_entry):
        board1= Board()
        have=test_entry[0]
        want=test_entry[1]
        for move in test_entry[0]:
            board1.setSlice(move[0],move[1],move[2])
            
        #print(board1)
        self.assertTrue(board1.checkWin())
    
  
    
    
        
if __name__ == '__main__':
    unittest.main()