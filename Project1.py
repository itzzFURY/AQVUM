import random

def gameplay():
    print("Welcome! Choose rock, paper or scissors!")
    option = ["rock", "paper", "scissors"]
    random_choice = random.choice(option)
    win_counter = 0
    tries_counter = 0
    
    while True:
        move = input("Enter your choice: ")

        if move.lower() in option: 
        
            print("Computer chose "+ random_choice)
            if move.lower() == random_choice:
                print("Tie")
                tries_counter = tries_counter + 1 
            elif move.lower() == "scissors" and random_choice == "paper":
                print("You win!")
                win_counter = win_counter + 1
                tries_counter = tries_counter + 1 
            elif move.lower() == "scissors" and random_choice == "rock":
                print("You lose!")
                tries_counter = tries_counter + 1 
            elif move.lower() == "paper" and random_choice == "scissors":
                print("You lose!")
                tries_counter = tries_counter + 1 
            elif move.lower() == "paper" and random_choice == "rock":
                print("You win!")
                win_counter = win_counter + 1
                tries_counter = tries_counter + 1 
            elif move.lower() == "rock" and random_choice == "scissors":
                print("You win!")
                win_counter = win_counter + 1
                tries_counter = tries_counter + 1 
            elif move.lower() == "rock" and random_choice == "paper":
                print("You lose!")
                tries_counter = tries_counter + 1 
        else:
            print("Invalid choice.") 

        retry = input("Retry? (y/n): ")
        if retry.lower() != "y":
            print("You won", win_counter, "out of ", tries_counter,"tries")
            print("Goodbye!")
            break
       
gameplay ()
 


