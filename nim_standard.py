'''
Name: Daniel Adeyelu
Description: Game of nim
Date: 12th January 2023
'''
import random
# Initialize the player and computer scores to 0
player = 0
computer = 0

# Initialize a variable to store the subtracted number
subtracted_number = 0

# Initialize a variable to store the player's input
player_input = 0

# Initialize a range for the game
game_range = random.randint(30,50)

# Initialize a range for the selection
selection_range = range(1,4)

# Initialize a flag to indicate if the game is continuing
is_continuing = True

# Print the game range
print("Game range is {}".format(game_range))

# Start a while loop to play the game
while is_continuing:
    try:
        # Ask the user to input a number between 1 and 3
        user_input = int(input("Select a number between 1-3: "))

        # Print a separator line
        print("*******************************************************")

        # Print the user's input
        print("User selected {}".format(user_input))

        # Subtract the user's input from the game range to get a new game range
        game_range = game_range - user_input

        # Print the new game range
        print("New Game range is {}".format(game_range))

        # Print another separator line
        print("_______________________________________________________")

        # If the new game range is greater than 0, it's the computer's turn
        if game_range > 0:
            # Determine the computer's input based on the new game range
            if game_range <= 9:
                computer_input=3
            if game_range <= 3:
                computer_input=2
            if game_range == 10:
                computer_input=1

            if game_range==11:
                computer_input=2

            if game_range==12:
                computer_input=3

            if game_range >= 13:
                # If the game range is greater than or equal to 13, the computer's input is a random number between 1 and 3
                computer_input = random.randint(1,3)

            # Print the computer's input
            print("Computer selected {}".format(computer_input))

            # Subtract the computer's input from the game range to get a new game range
            game_range = game_range - computer_input

            # Print the new game range
            print("New Game range is {}".format(game_range))

            # Print another separator line
            print("_______________________________________________________")

            # If the new game range is less than or equal to 0, the user wins
            # If is_continuing is set to false, stop looping
            if game_range <= 0:
                print("YOU WIN")
                is_continuing = False
        # If the user input is less than or equal to 0, the user loses        
        elif user_input <= 0:
            print("YOU LOSE")
            is_continuing = False
        # If the new game range is less than 1, the user losers
        elif game_range < 1:
            print("YOU LOSE")
            is_continuing = False
    except:
        print("Invalid Entry!!! Try Again")
