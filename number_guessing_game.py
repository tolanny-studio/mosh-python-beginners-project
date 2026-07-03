import random

highest_number = 100
lowest_number = 1

random_number = random.randint(lowest_number, highest_number)

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        
    except ValueError:
        print("Please enter a valid number!")
        continue
    
    if guess > 100 or guess < 0:
      print("Number is negative!!! Retry")    
      continue
    elif guess == random_number:
        print("You guessed right!")
        break
    elif guess > random_number:
        print("Too high")
    else:
        print("Too low")
