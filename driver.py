from Game import *
from User import *
from uuid import uuid4

if __name__ == "__main__":
    
    print("Jankey Tic Tac Toe API v0.5")
    print("---")
    
    p1=raw_input("Print Player 1 Name:")
    p2=raw_input("Print Player 2 Name:")

    boardy = Board()
    boardy.save()

    game = Game(board=boardy)
    gc = GameController(game)
   
    player1 = User(name=str(p1),uid=str(uuid4()))
    player2 = User(name=str(p2),uid=str(uuid4()))

    player1.save()
    player2.save()

    gc.setUser(str(player1.uid),1)
    gc.setUser(str(player2.uid),2)
    
    winner=False
    while(winner==False):
        move_index=int(raw_input("Enter Move :"))
        
        #print gc.game
        #print gc.game.board 
        
        winner=gc.move(move_index)

        print(game.state)
        if(winner=="invalid"):
            print("Invalid Move. Try again")
            winner=False
            continue
        
        if(winner):
            print("Winner!!!!")
            print(winner.name)
            
        
