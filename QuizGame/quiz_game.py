

score = 0
print ("Welcome to quiz game")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay, lets play!")

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")


answer = input("What does GPU stand for? ").lower()
if answer == "graphic processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")


answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")


answer = input("What does PSU stand for? ").lower()
if answer == "power supply":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print(score)