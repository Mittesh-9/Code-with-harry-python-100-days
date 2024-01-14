import random

computer_plays = ["snake", "water", "gun"]

score = 0

print("Welcome to the Snake Water Gun game")

win_results_dict = {
    "gun_snake": "You win",
    "water_gun": "You win",
    "snake_water": "You win",
}

lose_results_dict = {
    "snake_gun": "You loose",
    "gun_water": "You loose",
    "water_snake": "You loose"
}

tie_results_dict = {
    "gun_gun": "It's a tie",
    "snake_snake": "It's a tie",
    "water_water": "It's a tie"
}

while True:
    user_choice = input("Choose your Play 'Snake' 'Water' 'Gun' OR enter 'E' to exit the game : ")
    computer_choice = ''.join(random.choices(computer_plays))
    
    condition = f"{user_choice}_{computer_choice}"

    if condition in win_results_dict:
        score += 1
        print(f"Computer plays : {computer_choice}")
        print(win_results_dict[condition], f"Your score is {score}")
        
    elif condition in lose_results_dict:
            score -= 1
            print(lose_results_dict[condition], f"Your score is {score}")

    elif condition in tie_results_dict:
                score += 0
                print(f"It's a tie. Your score is {score}")

    elif user_choice.lower() == "e":
          break

    else:
        print("Invalid Input")
        continue