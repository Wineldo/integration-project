"""A guessing game that allows the user to specify a range and predict the
number the program picked. The user will have additional help such as 'near'
or 'far' to approximate the program's number. The program will limit the
number of guesses based on the user's range."""
__author__ = "Wineldo Jean"


import math  # Necessary to perform complex calculation
import random  # Necessary for the 'Guess My Number' game


def learn(user):
    """
    Summary line:
    The integration project for Sprint One. It goes through all the
    Python basic calculations, string operators, shortcut operators,
    numeric operators, and simple I/O

    Parameters:
    user (str): the name of the user

    Returns:
    boolean: True after completing the program successfully
    """

    # Python mathematical symbol instructions
    print("\nOkay,", user)
    print("Let me teach you the basics since you are new.")
    print("We are going to start with Python mathematical symbols\n")

    # Numeric operator: ** represents the power rule (2^5)
    print("This ** represents the power rule in Python: 2**5 =", 2 ** 5)

    # Numeric operator: *  represents multiplication (2*5)
    print("This * represents multiplication in Python: 2*5 =", 2 * 5)

    # Numeric operator: /  represents division       (2/5)
    print("This / represents division in Python: 2/5 =", 2 / 5)

    # Numeric operator: %  represents modulo         (2%5)
    print("This %", "represents the modulo (division remainder) in Python:"
                    " 2%5 =", 2 % 5, )

    # Numeric operator: // represents division       (2//5)
    print("This // represents division (with no remainder) in Python:"
          " 2//5 =", 2 // 5)

    # Numeric operator: +  represents addition       (2+5)
    print("This + represents addition in Python: 2+5 =", 2 + 5)

    # Numeric operator: -  represents subtraction    (2-5)
    print("This - represents subtraction in Python: 2-5 =", 2 - 5)

    print("\nWe can use these mathematical symbols in a text or a string.\n")

    # String operator: * represents how times the string is repeated
    print("This * is used to indicate how many times a text is repeated.")
    word = str(input("For instance, please enter a word or a sentence: "))
    while True:
        try:
            repeat = int(input("How many times you wanted it repeated: "))
            break
        except ValueError:
            print("Error. Must be a whole number.")

    print("\n", word * repeat, "\n", sep='')

    # String operator: + represents concatenation or combination
    print("This + is used to combine two or more words in Python.")
    word = str(input("For example, please enter a word or a sentence: "))
    word2 = str(input("Please enter another word or a sentence: "))
    print("This is the result of combining two strings:", word + word2, "\n")

    print("Wow, that is a lot to learn but we are not done yet!")
    print("I am going to show you how to make a variable in Python.\n")

    # Assignment operator: = assign values to a variable
    print("This = symbol is completely different in Python.")
    print("This is use to attach a value to any particular variable")

    var = str(input("\nAs a demonstration, please type in a variable name: "))
    value = input("Think of anything you want the variable to be assign: ")

    print("Your variable", var, "=", value, "\n")

    print("Now, I think we are almost finish, is to give you useful tips\n")

    # Shortcut operators: += represents the incrementation
    print("This += increases any variable to its next number: 5 +=1 = 6")
    # Shortcut operators: -= represents the decremental
    print("This -= decreases any variable to its last number: 5 -=1 = 4")

    print("\nYou have now learned all the basics.")
    print("I hope you have found this useful.")

    return True


def answer(query):
    """
    Summary line:
    It prompts and takes the user's response and return True if user
    agrees with the question otherwise False

    Parameters:
    query (str): a question statement

    Returns:
    boolean: true or false based on user's response
    function: recall the function if user's response is undetermined
    """
    allow = ["1", "yes", "yeah", "yea", "y"]
    never = ["0", "no", "nope", "nah", "n"]

    select = input(query).strip()  # Receive the user's response

    for item in range(len(allow)):
        if allow[item] == select.lower():
            return True

    for item in range(len(never)):
        if never[item] == select.lower():
            return False

    print("\nI'm sorry but I could not understand your response.")
    print("Please try again.")
    return answer(query)  # Call the function again on unclear response


def game(setup, players):
    """
    Summary line:
    The core of the 'Guess My Number' game with complex logic

    Parameters:
    setup (arr): the procedure of the 'Guess My Number' game
    players (arr): the names of the people who are playing

    Returns:
    str: congratulating the winner and exiting the game
    function: play the game again with a new procedure
    """
    python = players[0]
    user = players[1]
    tries = math.ceil(abs(setup[1] - setup[2]) * 0.20)
    num = setup[0]
    won = python

    while tries > 0:
        print('\nThis is how many times you can guess:', tries)

        while True:
            try:
                guess = int(input('Predict my number: '))
                break
            except ValueError:
                print("Error. Must be a whole number.")

        approx = abs(guess - num)
        scope = math.ceil(abs(setup[1] - setup[2]) * 0.20)

        if guess > setup[1] or guess < setup[2]:
            print('\nYour guess number is outside of range')
            print('Please, try again.')
        elif approx > scope:
            print('\nYour guess is too far from my number.')
            print('Try getting closer.')
            tries -= 1
        elif scope >= approx > 0:
            print('\nYour guess is near my number.')
            print('Proceed with caution!')
            tries -= 1
        else:
            print('\nCongratulations, ', user, '!', sep='')
            print('You\'ve guessed my number!')
            tries = 0
            won = user

    if won == python:
        print('\nYou have no more tries. My number was', num)
        print('Hee, I guess I won this round.')

    if not answer('\nWould you like to play again (Y/N)?\n'):
        return print('\nThanks for playing!')

    return game(random_number(), players)


def random_number():
    """
    Summary line:
    This is responsible for returning a random number within the range
    specify by the user

    Parameters:
    none

    Returns:
    arr: a list of the guess number, and the range such as initial and final
    """

    print('\nPlease pick the range for the \'Guess My Number\' game\n')

    while True:
        try:
            initial = int(input('From: '))
            final = int(input('To: '))
            break
        except ValueError:
            print("Error. Must be a whole number.")

    if final < initial:
        print('\nRange complexion error.')
        print('Try entering it from least to greatest.\n')
        return random_number()

    if final == initial:
        print('\nRange complexion error.')
        print('The numbers are the same with no difference.\n')
        return random_number()

    return [random.randint(initial, final), final, initial]


def welcome():
    """
    Summary line:
    New member is greeted with an introduction message and
    will register his/her name to system

    Parameters:
    none

    Returns:
    arr: a list of python's name and user chosen name.
    """

    # A list of names for the program to choose
    names = ["Jon", "Bill", "Maria", "Jenny", "Jack", "Michael"]

    python = names[random.randint(0, len(names) - 1)]
    print("Welcome, I'm ", python, "!", sep='')
    print("I will be guiding you throughout the process.")

    print("\nHmm. You look awfully familiar.")
    user = input("I think your name is: ").capitalize()

    print("\nThat's right, You're ", user, "!", sep='')
    print("I've heard a lot about you!")

    return [python, user]


def main():
    """
    Summary line:
    Initialize the following program.

    Parameters:
    none

    Returns:
    function: initiate the game()
    """
    participant = welcome()  # Return a list of the names
    if answer("\nDo you know Python (Y/N)?\n") or learn(participant[1]):
        print("\nAll right, now that you've made it here")
        print("Let's get started with the game!")
        return game(random_number(), participant)


main()
