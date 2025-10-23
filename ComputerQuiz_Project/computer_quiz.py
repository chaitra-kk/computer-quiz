# -------------------------------
# Computer Quiz Game by Chaitra 
# -------------------------------

# Welcome message
print("Welcome to my computer quiz!")

# Asking if the user wants to play
playing = input("Do you want to play? ")

# Initialize score
score = 0

# Check if the user wants to play
if playing.lower() != "yes":
    print("Okay, bye 👋")
    exit()

print("Okay, let's play! 😊")

# Question 1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Yay, correct! 🎉")
    score += 1
else:
    print("Wrong answer 😢")
    print("It's 'Central Processing Unit'!")

# Question 2
answer = input("What does GUI stand for? ")
if answer.lower() == "graphical user interface":
    print("Good going! 😄")
    score += 1
else:
    print("Wrong answer 😬")
    print("It's 'Graphical User Interface'!")

# Question 3
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Not bad! 😎")
    score += 1
else:
    print("Wrong answer 😕")
    print("It's 'Graphics Processing Unit'!")

# Show score if user wants
your_score = input("Do you want to see your score? ")
if your_score.lower() == "yes":
    print("You have scored:", score)
    print("You got " + str(score) + " questions correct!")
    print("Your score: " + str((score / 3) * 100) + "% 🎯")

print("Thanks for playing! 💖")
