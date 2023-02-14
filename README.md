# Game of Nim
A mathematical game of strategy in which two players take turns subtracting numbers from a random range. On each turn, a player must remove a range of numbers between 1 and 3 inclusively, once the random game range is 0 or less than 0, the other player wins

# The Standard Game
The code implements the game of nim. It starts by printing a random number within the range of 20 to 30 as the game range. The user is then asked to input a number between 1 to 3, and this input is subtracted from the game range to get a new game range. If the new game range is greater than 0, the computer's turn starts. The computer's turn involves selecting a number between 1 and 3, which is then subtracted from the game range to get a new game range. The computer's input is determined using a series of if-elif conditions. If the game range becomes less than or equal to 0, the user wins. If the user's input is less than or equal to 0, the user loses. If the game range becomes less than 1, the user also loses. If the user inputs an invalid value, the code throws an exception, and the user is asked to try again.

# Using Reinforcement Learning
The script uses reinforcement learning to make the computer's moves. The reinforcement learning variables include the learning rate (alpha), the exploration rate (epsilon), and the state-action value table (Q). The function choose_action selects an action based on the current state and the exploration rate. The Q table is updated after each move based on the reward and the maximum Q value for the next state.

The script also keeps track of the player and computer scores, the number of plays, and offers the option to rematch after each game. If the player enters an invalid input, the script raises a ValueError with an error message. Overall, the script demonstrates a simple implementation of reinforcement learning in a game scenario.
