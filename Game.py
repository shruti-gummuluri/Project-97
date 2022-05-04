import random 
print("Guess the Number..!!")
num = random.randint(1,9)
chance = 0
print("Guess A Number Between 1 and 9: ")
while chance<5:
    guess = int(input("Enter A Number: "))
    if guess==num:
        print("Congratulations..!! You have won!")
        break
    elif guess<num :
        print("Your guess was too low")
    else:
        print("Your guess was too high")
    chance +=1
if not chance<5 :
    print("You Lose")
    