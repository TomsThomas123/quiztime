print('Welcome to the quiz of life.')
playing = input("Would you like you begin? ")
if playing != 'yes':
    quit
print("Okay! Let's play!")
score = 0
a1 = input('what does GPU stand for? ')
if a1 == "graphics processing unit":
    print('Correct!')
    score = score + 1
else:
    print('Incorrect!')
a1 = input('what does GPlU stand for? ')
if a1 == "graphics processing unit":
    print('Correct!')
    score = score + 1
else:
    print('Incorrect!')

a1 = input('what does GwPU stand for? ')
if a1.lower == "graphics processing unit":
    print('Correct!')
    score = score + 1
else:
    print('Incorrect!')

a1 = input('what does GPvU stand for? ')
if a1.lower == "graphics processing unit":
    print('Correct!')
    score = score + 1
else:
    print('Incorrect!')
print('You got ' + str(score) + "questions correct!")