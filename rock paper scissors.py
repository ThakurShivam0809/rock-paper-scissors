import random

def game():
    print("Enter 'r' for rock\nEnter 'p' for paper\nEnter 's' for scissors ")
    replay = 'yes'
    while replay == 'yes':
      comp = random.choice(['r','p','s'])
      user = input("Enter your choice: ")
      print(f"The computer had {comp}")
      if comp == 'r' and user == 'p':
          print("You won!")
      elif comp == 'p' and user == 's':
          print("You won!")
      elif comp == 's' and user == 'r':
          print('You Won!')
      elif comp == user :
          print("It's a draw")
      else:
          print("You loose")
      print("Do you want to play again; Type yes/no: ")
      replay = input()
game()
