from Game import *


if __name__ == "__main__":
    
    print("Jankey Tic Tac Toe API v0.5")
    print("---")
    
    p1=raw_input("Print Player 1 Name:")
    p2=raw_input("Print Player 2 Name:")
    
    game = Game()
    
    game.setUser(p1,1)
    game.setUser(p2,2)
    
    winner=False
    while(winner==False):
        move_index=int(raw_input("Enter Move:"))
        
        
        
        winner=game.move(move_index)
        if(winner=="invalid"):
            print("Invalid Move. Try again")
            winner=False
            continue
        
        if(winner):
            print("Winner!!!!")
            print(winner.getName())
            
        