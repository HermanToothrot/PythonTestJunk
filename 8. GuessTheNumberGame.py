import random as r
secretnumber= r.randint(-5, 5)
 
attemptsmade=0
while attemptsmade <6:
    print("Guess the number")
    try:
        guess = str(input())
        if guess=="?":
            print(f"The secret number is {secretnumber}")
        elif int(guess) < secretnumber:
            print("Higher")
            attemptsmade+=1
        elif int(guess) > secretnumber:
            print("Lower")
            attemptsmade+=1
        else:
            break
            
    except ValueError:
        print("Enter a numeric value.")

if guess==str(secretnumber):
    print("Number guessed in "+str(attemptsmade)+" attempts.")
else:
   print("The number was "+str(secretnumber))
