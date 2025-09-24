print("hello DAFS-FT-14!")
print("🏆")

# Add a code to my script, please be nice
# Bravo DAFS15!

# Question 1
lives = 3

quest_1 = float(input("What is 4-1?"))
while quest_1 != 3:
    lives -= 1
    if lives == 0:
        print("You lose!")
        break
    quest_1 = float(input("Wrong answer, please try again. What is 4-1?"))

print(f"You answered: {round(quest_1)}")


# Question 2
if lives > 0:
    quest_2 = float(input("What is the square root of 25?"))
    while quest_2 != 5:
        lives -= 1
        if lives == 0:
            print("You lose!")
            break
        quest_2 = float(input("Wrong answer, please try again. What is the square root of 25?"))

    print(f"You answered: {quest_2}")


# Question 3
if lives > 0:
    quest_3 = input("Who is the CEO of Tesla and SpaceX?").lower()
    while quest_3 != "elon musk":
        lives -= 1
        if lives == 0:
            print("You lose!")
            break
        quest_3 = input("Wrong answer, please try again. Who is the CEO of Tesla and SpaceX?").lower()

    print(f"You answered: {quest_3}")

print("Well done!")
     
