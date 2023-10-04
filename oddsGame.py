import random
random = random.randint(1,10)
number = int (input("Chose a number from 1 to 10: "))
while True:
    error = ""
    
    if random != number:
        error = "Its wrong"
    if number > 10: 
        error = "The number needs to be under 10"
    elif number < 1: 
        error = "The number needs to be over 1"
    
    if error == "":
        break
    
    print(error)
    error = ""
    number = int (input("Chose a number from 1 to 10: "))
print("You got it!")
