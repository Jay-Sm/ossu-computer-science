# an_letters = "aefhilmnorsxAEFHILMNORSX"

# word = input('I will cheer for you! Enter a word: ')
# times = int(input('Enthusiasm level (1-10): '))

# for char in word:
#     if char in an_letters:
#         print("Give me an", char.upper() + '!')
#     else:
#         print("Give me a", char.upper() + '!')

# print('\nWhat does that spell?')
# for i in range(times):
#     print(word.upper() + '!!!')


### Cube Root Guess and Check
cube = 8
cube = abs(cube)

for guess in range(cube + 1):
    if guess**3 >= cube:
        break

if guess**3 != cube:
    print(cube, 'is not a perfect cube')
elif cube < 0:
    guess = -guess
else:
    print('Cube root of', str(cube), 'is', str(guess))
print('\n')

### Approximate Solution Guess and Check
cube = 8 
epsilon = 0.01
guess = 0.0
increment = 0.0001
guess_num = 0

while abs(guess**3 - cube) >= epsilon and abs(guess <= cube):
    guess += increment
    guess_num += 1

print('Number of guesses is', guess_num)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)

# Bisection Search
