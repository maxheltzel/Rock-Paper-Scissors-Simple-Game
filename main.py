import random
print("This is a simple random rpc generator created By Nabeel Arif and Max Heltzel")
decisions = ["rock", "paper", "scissors"]
opposition = decisions[random.randint(0, 2)]
player = input("Hurry up and make a move dummy: ").lower()

print("Computer plays " + opposition)
if player == "s":
	if opposition == "p":
		print("You Lost darling!")
	else:
		print("You Won Bruh")
elif player == "r":
	if opposition == "paper":
		print("You Lost darling!")
	else:
		print("You Won Bruh!")
elif player == "p":
	if opposition == "scissor":
		print("You Lost darling!")
	else:
		print("You Won Bruh!")


#Add functionality for life points, if you lose three times, then your lifes go away and game ends