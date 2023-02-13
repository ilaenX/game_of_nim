'''
Name: Daniel Adeyelu
Description: Game of nim using reinforcement learning (Q-table)
Date: 26th January 2023
'''

import random
import numpy as np

player = 0
computer = 0
subtracted_number = 0
player_input = 0
game_range = random.randint(40,60)
selection_range = range(1,4)
is_continuing = True
user_score = 0
computer_score = 0

# Reinforcement learning variables
alpha = 0.8 # learning rate
epsilon = 1 # exploration rate
Q = np.zeros((100, 4)) # state-action value table

def choose_action(state, epsilon):
    if np.random.uniform(0, 1) < epsilon:
        # Choose random action with exploration rate epsilon
        return np.random.choice(selection_range)
    else:
        # Choose action with highest value in Q table
        return np.argmax(Q[state, :])


print("Game range is {}".format(game_range))
num_plays = 0
while is_continuing:
    try:
        user_input = int(input("Select a number between 1-3: "))
        if user_input not in selection_range:
            raise ValueError("Invalid Entry!!! Try Again")
        print("*******************************************************")
        print("User selected {}".format(user_input))
        game_range = game_range - user_input
        print("New Game range is {}".format(game_range))
        print("_______________________________________________________")
        if game_range > 0:
            # Update exploration rate based on number of games played
            if game_range == 2:
              computer_input = 1
            if num_plays < 20:
                epsilon = 1
            elif num_plays < 40:
                epsilon = 0.5
            else:
                epsilon = 0.1
            computer_input = choose_action(game_range, epsilon)

            print("Computer selected {}".format(computer_input))
            game_range = game_range - computer_input
            print("New Game range is {}".format(game_range))
            print("_______________________________________________________")
            if game_range <= 0:
                reward =+ 1
                user_score =+ reward
                print("YOU WIN")
                print("-------------------")
                rematch = input("Do you want to rematch? (Y/N)")
                print("Number of plays: {}" .format(num_plays))
                print("-------------------")
                if rematch == "Y" or "y" or "yes" or "Yes":
                    game_range = random.randint(40,60)
                    num_plays=+1
                    is_continuing = True
                elif rematch == "N" or 'n' or 'no' or "No":
                    is_continuing = False
                    print("YOU WIN")
                    print("Number of plays: {}" .format(num_plays))
                    print("Player: {} \t\t Computer: {}".format(user_score, computer_score))
                    break
                    # is_continuing = False
                
            else:
                reward = -1
            # Update Q table
            Q[game_range + user_input + computer_input, computer_input] = (1 - alpha) * Q[game_range + user_input + computer_input, computer_input] + alpha * (reward + np.max(Q[game_range, :]))
        elif user_input <= 0:
            computer_score =+ reward
            print("YOU LOSE")
            reward = -1
            print("-------------------")
            rematch = input("Do you want to rematch? (Y/N)")
            print("Number of plays: {}" .format(num_plays))
            print("-------------------")
            if rematch == "Y" or "y" or "yes" or "Yes":
                game_range = random.randint(40,60)
                num_plays=+1
                is_continuing = True
            elif rematch == "N" or 'n' or 'no' or "No":
                is_continuing = False
                print("YOU WIN")
                print("Number of plays: {}" .format(num_plays))
                print("Player: {} \t\t Computer: {}".format(user_score, computer_score))
                break
                
        elif game_range < 1:
            computer_score =+ reward
            print("YOU LOSE")
            reward = -1
            print("-------------------")
            rematch = input("Do you want to rematch? (Y/N)")
            print("Number of plays: {}" .format(num_plays))
            print("-------------------")
            if rematch == "Y" or "y" or "yes" or "Yes":
                game_range = random.randint(40,60)
                num_plays=+1
                is_continuing = True
            elif rematch == "N" or 'n' or 'no' or "No":
                is_continuing = False
                print("YOU WIN")
                print("Number of plays: {}" .format(num_plays))
                print("Player: {} \t\t Computer: {}".format(user_score, computer_score))
                break
    except ValueError as ve:
        print(ve)
