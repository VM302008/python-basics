print("Welcome to my country quiz!")

playing = input("Do you want to play? \n")
if playing.lower() != "yes":
    quit()

print("Ok, let's play! ")
score = 0

answer = input("What is the smallest country in the world? \n")
if answer.lower() == "vatican city":
    print("Correct!")
    score += 1
else:
    print("Inconrrect!")

answer = input("HWhat is the biggest country in the world? \n")
if answer.lower() == "russia":
    print("Correct!")
    score += 1
else:
    print("Inconrrect!")

answer = input("How many countries have their capital city in Europe? \n")
if answer.lower() == "44":
    print("Correct!")
    score += 1
else:
    print("Inconrrect!")

answer = input("WWich continent is missing: Africa; North America; South America; Antartica; Europe; Oceania? \n")
if answer.lower() == "asia":
    print("Correct!")
    score += 1
else:
    print("Inconrrect!")

print("\nYou got " + str(score) + "/4 questions")
print("You got " + str(score / 4 * 100) + "/%")