from logging import PlaceHolder
import random

while True:

    choices=['R', 'P', 'S']
    player= input("Rock[R], Paper[P], Scissors[S]??: ").upper()
    
    if player=='R':
        player_choice='rock'
    elif player=='P':
        player_choice='paper'
    elif player=='S':
        player_choice='scissors'
        
    computer=random.choice(choices)
    if computer=='R':
        computer_choice='rock'
    elif computer=='P':
        computer_choice='paper'
    elif computer=='P':
        computer_choice='scissors'

    print(f"\nYou chose; {player} and the Computer chose; {computer}.\n")

    if player==computer:
        print(f"Both players selected{player}.It's a tie!")
    elif player=='R':
        if computer=='S':
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player=='P':
        if computer=='R':
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif player=='S':
        if computer=='P':
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
            
    if player not in choices:
        print("Error, pick a valid option")
     
    play_again=input("\n\nDo you wish to play again? (yes/no): ")
    if play_again=="yes":
      print("player()")
    else:
        break

    
       
