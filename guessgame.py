import random 

random_number = random.randint(1,10)
guess = None

while guess != random_number:
	guess = input("pick a number between 1 and 10:")
	guess = int(guess)
	if guess < random_number:
		print("TOO LOW!") 
	elif guess > random_number:
		print("too High!!")
	else: 
		print("You Won !!!!!")

print(random_number)