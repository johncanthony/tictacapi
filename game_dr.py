#!/usr/bin/python

from Game import *
from User import *
from uuid import uuid4
from Board import *
import hashlib
import sys

def login():
    test_user = str(raw_input("Enter Username- "))

    
    b =  User.objects.filter(name=test_user)
    
    if(len(b) < 1):
        print("User not found")
        return False
    else:
        user = b[0]


    test_passwd=hashlib.sha256(str(raw_input("Enter Password- ")))

    if(test_passwd.hexdigest() == str(user.passwd)):
        return user
    else:
        return False

def create_game(player):

    board = Board()
    board.save()

    g = Game(board=board)
    gc = GameController(g)

    gc.setUser(str(player.uid))


    if(g.is_valid()):
        g.save()
        print("Game created successfully. Waiting for player 2...")
    else:
        print("invalid")

def join_game(player):
    
      users_ex = [str(player.uid),str(-1)]
      games = Game.objects.filter(state=0)

      for game in games:
          if str(player.uid) in game.player1:
              continue
          else:
              game_con = GameController(game)
              game_con.setUser(str(player.uid))
              game.save()
              print("Joined game. It's player one's move.")
              break


def list_games(player):

    p1_selected_games = Game.objects.filter(player1=player.uid)
    p2_selected_games = Game.objects.filter(player2=player.uid)

    for each in p1_selected_games:
      
        if each.state>2:
            continue

        p2 = User.objects.filter(uid=each.player2)
       
        if(len(p2) == 0):
            opponent = "Pending...."
        else:
            opponent = p2[0].name
        
        print("{} : Opponent - {}".format(each.id,opponent))

    for each in p2_selected_games:

        if each.state>2:
            continue

        p1 = User.objects.filter(uid=each.player1)[0]
        print("{} : Opponent - {}".format(each.id,p1.name))


def make_move(player, game):

    
    if(game.state == 0):
        print("Game still finding player2")
        return
    

    move_index=int(raw_input("Enter Move :"))

    gc = GameController(game)

    winner=gc.move(move_index)

    if(winner=="invalid"):
        print("Invalid Move. Try again")
        winner=False

    if(winner):
        print("Winner!!!!")
        print(winner) 

if __name__ == "__main__":
    
    print("Jankey Tic Tac Toe API v0.5")
    print("---")

    user = login()

    if not user:
        sys.exit(0)

    choice = -1

    while(choice!=5):

        print("== User : {} ==".format(user.name))
        print("1) Create Game")
        print("2) Join Game")
        print("3) List my games")
        print("4) Make move")
        print("5) Exit")

        choice = int(raw_input(":"))

        if choice == 1:

            create_game(user)

        elif choice == 2:
        
            join_game(user)

        elif choice == 3:

            list_games(user)

        elif choice == 4:
            print("Choose game to move:")
            list_games(user)

            id_num = int(raw_input("Enter you game selection:"))

            game = Game.objects.get_by_id(id_num)

            if(game == None):
                print("Game no longer available")
                sys.exit(1)
        

            if((game.player1 == str(user.uid)) and (game.state == 2)):
                print("Not your play")
                sys.exit(1)

            elif((game.player2 == str(user.uid)) and (game.state==1)):
                print("Not your play")
                sys.exit(1)
        

            make_move(user,game)
