import random

def user_choice():
    print("Enter your choice: Snake (s), Water (w), Gun (g)")
    user_choice = input().lower()
    return user_choice

def computer_choice():
    choices = ['s', 'w', 'g']
    computer_choice = random.choice(choices)
    return computer_choice

def Determine_winner(user,computer):
    if user == computer:
        return "It's a Tie!"
    elif user == "s":
        if computer == "w":
            return "You win! Snake drinks Water."
        else:
            return "Computer wins! Gun shoots Snake."
    elif user == "w":
        if computer == "g":
            return "You win! Water douses Gun."
        else:
            return "Computer wins! Snake drinks Water."
    elif user == "g":
        if computer == "s":
            return "You win! Gun shoots Snake."
        else:
            return "Computer wins! Water douses Gun."

def play_game():
    
    while True:
        user = user_choice()
        if user not in ['s', 'w', 'g']:
            print("Your input is invalid! Please enter 's', 'w' or 'g'")
            continue
        
        computer = computer_choice()
        print(f"Your choies is {user}")
        print(f"Computer choies is {computer}")
        
        result = Determine_winner(user,computer)
        print(result)

        play_again = input("Do you want to play again? (yes/no) ").lower()
         
        if play_again in ["no","n","not"]:
            break

        
    print("Thanks for playing!")

# if __name__ == "__main__":
play_game()


# import random

# def get_user_choice():
#     print("Enter your choice: Snake (s), Water (w), Gun (g)")
#     user_choice = input().lower()
#     return user_choice

# def get_computer_choice():
#     choices = ['s', 'w', 'g']
#     computer_choice = random.choice(choices)
#     return computer_choice

# def determine_winner(user_choice, computer_choice):
#     if user_choice == computer_choice:
#         return "It's a tie!"
#     elif user_choice == 's':
#         if computer_choice == 'w':
#             return "You win! Snake drinks Water."
#         else:
#             return "Computer wins! Gun shoots Snake."
#     elif user_choice == 'w':
#         if computer_choice == 'g':
#             return "You win! Water douses Gun."
#         else:
#             return "Computer wins! Snake drinks Water."
#     elif user_choice == 'g':
#         if computer_choice == 's':
#             return "You win! Gun shoots Snake."
#         else:
#             return "Computer wins! Water douses Gun."

# def play_game():
#     user_score = 0
#     computer_score = 0

#     while True:
#         user_choice = get_user_choice()
#         if user_choice not in ['s', 'w', 'g']:
#             print("Invalid choice. Please enter 's', 'w', or 'g'.")
#             continue

#         computer_choice = get_computer_choice()
#         print(f"You chose {user_choice}")
#         print(f"Computer chose {computer_choice}")

#         result = determine_winner(user_choice, computer_choice)
#         print(result)

#         if "You win!" in result:
#             user_score += 1
#         elif "Computer wins!" in result:
#             computer_score += 1

#         print(f"Your Score: {user_score}")
#         print(f"Computer Score: {computer_score}")

#         play_again = input("Do you want to play again? (yes/no): ").lower()
#         if play_again != 'yes':
#             break

#     print("Thanks for playing!")

# if __name__ == "__main__":
#     play_game()