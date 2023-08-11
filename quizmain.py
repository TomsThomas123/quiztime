print('Welcome to the quiz of life.')
playing = input("Would you like you begin? ")
if playing != 'yes':
    quit
print("Okay! Let's play!")
score = 0
a1 = input('What does GPU stand for? ')
if a1 == "graphics processing unit":
    print('Correct!')
    score = score + 1
else:
    print('Incorrect!')
a1 = input('Who is the most popular Youtuber? ')
if a1 == "MrBeast":
    print('Correct!')
    score = score + 1
else:
    print('Incorrect!')

a1 = input('What is the fastest AMD CPU.? ')
if a1 == "Ryzen 9 7950X3D":
    print('Correct!')
    score = score + 1
else:
    print('Incorrect!')

a1 = input('What is the worlds most dangerous toy? ')
if a1. == "Hasbro Javelin Darts:
    print('Correct!')
    score = score + 1
else:
    print('Incorrect!')

print('You got ' + str(score) + "questions correct!")
