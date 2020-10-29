# Wineldo Jean - 29 October 2020 (last modified)
# A guessing game that allows the user to speficy a range and predict the number the program picked.
# The user will have additional help such as 'near' or 'far' to approximate the program's number.
# The program will limit the number of guesses based on the user's range.
# No source(s) available at this moment

import math, random

# A list of names for the program to choose
names = ['Jon', 'Bill', 'Maria', 'Jenny', 'Jack', 'Michael']

python = names[random.randint(0,len(names)-1)]
print('Welcome, I\'m ',python, '! \nI will be guiding you throughout the process.',sep='')

user = input('\nMhmmm. You look awfully familiar.\nI think your name is: ').capitalize()
print('\nYes, that\'s right! You\'re ',user,'! I have heard a lot about you.\nWait, let me make sure I got the right person...',sep='')

# The function learn() is the project for Sprint One
def learn():
    # Python mathematical symbol intrustions
    print('\nOkay, ',user,', let me teach you the basics since you are new to Python.',sep='')
    print('We are going to start with Python mathematical symbols\n')

    # Numeric operator: ** represents the power rule (2^5)
    print('This ** represents the power rule in Python: 2**5 =',2**5)

    # Numeric operator: *  represents mulitpilcation (2*5)
    print('This * represents mulitpilcation in Python: 2*5 =',2*5)

    # Numeric operator: /  represents division       (2/5)
    print('This / represents division in Python: 2/5 =',2/5)

    # Numeric operator: %  represents modulo         (2%5)
    print('This %', 'represents the modulo (division remainder) in Python: 2%5 =',2%5,)

    # Numeric operator: // represents division       (2//5)
    print('This // represents division (with no remainder) in Python: 2//5 =',2//5)

    # Numeric operator: +  represents addition       (2+5)
    print('This + represents addition in Python: 2+5 =',2+5)

    # Numeric operator: -  represents subtraction    (2-5)
    print('This - represents subtraction in Python: 2-5 =',2-5)

    print('\nWe can use these mathematical symbols in a text or a string as a programmer would say.\n')

    # String operator: * represents how times the string is repeated
    print('This * is used to indicate how many times a text is repeated in Python.')
    word   = str(input('For instance, please enter a word or a sentence: '))
    repeat = int(input('How many times you wanted it to be repeated: '))
    print('\n',word * repeat,'\n',sep='')   

    # String operator: + represents concatenation or combination 
    print('This + is used to combine two or more words in Python.')
    word  = str(input('For example, please enter a word or a sentence: '))
    word2 = str(input('Please enter another word or a sentence: '))
    print('Space is not added. This the result of combining a string:',word+word2,'\n')

    print('Wow, that is a lot to learn but we are not done yet!')
    print('I am going to show you how to make a variable in Python.\n')

    # Assignment operator: = assign values to a variable 
    print('This = symbol is completely different in Python.')
    print('This is use to attach a value to a variable user')
    var   = str(input('As a demostration, please enter any user to be use as a variable: '))
    value = input('Think of anything you want the variable to be assign: ')
    print('Your variable',var,'=',value,'\n')

    print('Now, I think we are almost finish, is to give you useful tips and advice\n')

    # Shortcut operators: += represents the incrementation 
    print('This += increases any variable to its next level or number: 5 +=1 = 6')
    # Shortcut operators: -= represents the decrementation 
    print('This -= decreases any variable to its lower level or number: 5 -=1 = 4')

    print('\nYou have now learned all the basics\nBye,',user,'\n')

    return True

# The function answer() takes the user's response and return True if user agrees with the question
def answer(query):
    allow = ['yes','yea', 'y', 'yeah']
    never = ['no', 'nope', 'nah', 'n']
       
    select = input(query).strip()

    for item in range(len(allow)):
        if allow[item] == select.lower():
            return True

    for item in range(len(never)):
        if never[item] == select.lower():
            return False

    print('\nI\'m sorry but I could not understand your response.\nPlease try again.')
    return answer(query)

# The function rules() showcases what is allow and not allow from playing the 'Guess My Number' game
def rules():
    print('\nThe rule has not been set in place yet.')

# The function game() is the 'Guess My Number' game with complex logic
def game(setup):
    tries = math.ceil(abs(setup[1] - setup[2]) * 0.20)
    num = setup[0]
    won = python

    while tries > 0:
        print('\nThis is how many times you can guess:',tries)
        guess = int(input('Predict my number: '))

        approx = abs(guess - num)
        scope = math.ceil(abs(setup[1] - setup[2]) * 0.20)

        if guess > setup[1] or guess < setup[2]:
            print('\nYour guess number is outside of range')
            print('Please, try again.')
        elif approx > scope:
            print('\nYour guess is too far from my number.')
            print('Try getting closer.')
            tries -= 1
        elif approx <= scope and approx > 0:
            print('\nYour guess is near my number.')
            print('Proceed with caution!')
            tries -= 1
        else:
            print('\nCongratulations, ',user,'!',sep='')
            print('You\'ve guessed my number!')
            tries = 0
            won = user

    if won == python:
        print('\nYou have no more tries. My number was',num)
        print('Hehe, I guess I won this round.')

    if answer('\nWould you like to play again?\n'):
        return game(random_number())
    else:
        return '\nThanks for playing!'

# The function random_number() is responsible for returning a number within the range specify randomly 
def random_number():
    print('\nPlease pick the range for the \'Guess My Number\' game\n')
    initial = int(input('From: '))
    final = int(input('To: '))

    if final < initial:
        print('\nRange complexion error.')
        print('Try entering it from least to greatest.\n')
        return random_number()

    if final == initial:
        print('\nRange complexion error.')
        print('The numbers are the same with no difference.\n')
        return random_number()
    
    return [random.randint(initial,final), final, initial]

if answer('\nAre you famailiar with Python?\n'): 
    print('\nAwesome, Let\'s get started!')
    print('The winner takes it all.')
    game(random_number())
else:
    learn()