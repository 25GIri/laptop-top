import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    
    print("Welcome to Rock, Paper, Scissors with Score Tracking!")
    print("Type 'quit' to exit the game.\n")
    
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit'): ").lower()
        
        if user_choice == 'quit':
            print("\nFinal Scores:")
            print(f"You: {user_score}")
            print(f"Computer: {computer_score}")
            print("Thanks for playing!")
            break
            
        if user_choice not in choices:
            print("Invalid choice. Please try again.\n")
            continue
            
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!\n")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win this round!\n")
            user_score += 1
        else:
            print("Computer wins this round!\n")
            computer_score += 1
            
        print(f"Score -> You: {user_score} | Computer: {computer_score}\n")

if __name__ == "__main__":
    play_game()
