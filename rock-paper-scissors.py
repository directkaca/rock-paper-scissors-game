import random

print("Welcome to Rock - Paper - Scissors Game")
print("We can begin the game NOW !!!\n\n")

rock = '''
 ____   ___     __  __  _ 
|    \ /   \   /  ]|  |/ ]
|  D  )     | /  / |  ' / 
|    /|  O  |/  /  |    \ 
|    \|     /   \_ |     \ 
|  .  \     \     ||  .  |
|__|\_|\___/ \____||__|\_|
                        '''

paper = '''
 ____   ____  ____   ___  ____  
|    \ /    ||    \ /  _]|    \ 
|  o  )  o  ||  o  )  [_ |  D  )
|   _/|     ||   _/    _]|    / 
|  |  |  _  ||  | |   [_ |    \ 
|  |  |  |  ||  | |     ||  .  \ 
|__|  |__|__||__| |_____||__|\_|
                                '''

scissors = '''
  _____   __  ____ _____ _____  ___   ____    _____
 / ___/  /  ]|    / ___// ___/ /   \ |    \  / ___/
(   \_  /  /  |  (   \_(   \_ |     ||  D  )(   \_ 
 \__  |/  /   |  |\__  |\__  ||  O  ||    /  \__  |
 /  \ /   \_  |  |/  \ |/  \ ||     ||    \  /  \ |
 \    \     | |  |\    |\    ||     ||  .  \ \    |
  \___|\____||____|\___| \___| \___/ |__|\_|  \___|
                                                   '''

paket = [paper, rock, scissors]
print("You choose: | (1) Rock | (2) Paper | (3) Scissors | \n")
pilihan = input("=> ").strip().lower()

if pilihan == "rock" or pilihan == "1":
    print(rock)
elif pilihan == "paper" or pilihan == "2":
    print(paper)
elif pilihan == "scissors" or pilihan == "3":
    print(scissors)
else:
    print("Your input is invalid, please try again")

print("Computer choice: \n")
computer_choice = random.choice(paket)
print(computer_choice)

if pilihan == 'rock' or pilihan == "1" and computer_choice == rock:
    print("\nDraw - It's just coincidence")
elif pilihan == 'rock' or pilihan == "1" and computer_choice == paper:
    print("\nSorry, you lose")
elif pilihan == 'rock' or pilihan == "1" and computer_choice == scissors:
    print("\nYeaay, you did it")
elif pilihan == 'paper' or pilihan == "2" and computer_choice == paper:
    print("\nDraw - It's just coincidence")
elif pilihan == 'paper' or pilihan == "2" and computer_choice == scissors:
    print("\nSorry, you lose")
elif pilihan == 'paper' or pilihan == "2" and computer_choice == rock:
    print("\nYeaay, you did it")
elif pilihan == 'scissors' or pilihan == "3" and computer_choice == scissors:
    print("\nDraw - It's just coincidence")
elif pilihan == 'scissors' or pilihan == "3" and computer_choice == rock:
    print("\nSorry, you lose")
elif pilihan == 'scissors' or pilihan == "3" and computer_choice == paper:
    print("\nYeaay, you did it")





