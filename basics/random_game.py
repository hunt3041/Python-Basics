import random
# generate a number 1-10
random_num = random.randint(1, 10)
# input from user?
while True:
    user_guess = input('enter your guess')
    # check that the input is a number 1-10
    try:
        if type(int(user_guess)) == int and int(user_guess) >= 1 and int(user_guess) <= 10:
            user_guess = int(user_guess)
            if user_guess == random_num:
                print('Correct!')
                break
            else:
                print('wrong number, try again')
        else:
            print('Enter valid number')
    except ValueError:
        print('Invalid entry')

    # check if number is the right guess, otherwise ask again
