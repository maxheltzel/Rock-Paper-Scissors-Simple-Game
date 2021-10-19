import random
import turtle

print("Type 'scissors' for scissors 'rock' for rock and 'paper' for paper")
decisions = ["rock", "paper", "scissors"]

opposition = decisions[random.randint(0,2)]
player = input("Hurry up and make a move: ")

"""
this function dictates if the two imputs are equal. If so, the output
results in a tie
"""
print("Computer plays " + opposition)
if player == opposition:
  print("Both players selected " + opposition + " It's a tie!")
elif player == "scissors":
	if opposition == "paper":
		print("You Won!")
	else:
		print("You Lost darling")
elif player == "rock":
	if opposition == "paper":
		print("You Lost darling")
	else:
		print("You won!")
elif player == "paper":
	if opposition == "scissors":
		print("You Lost darling")
	else:
		print("You Won!")
