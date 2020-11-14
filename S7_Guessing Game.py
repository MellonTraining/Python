import random
computers_number = random.randint(1,50)
prompt = 'What is your guess? '
while True:
    players_guess = input(prompt)
    if computers_number == int(players_guess):
        print("Correct")
        break
    elif computers_number > int(players_guess):
        print("too low")
    else:
        print("too high")
    	

    

   
