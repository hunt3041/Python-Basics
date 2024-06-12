# Error Handling

while True:
    try:
        age = int(input('what is your age?'))
        10/age

    except ValueError:
        print('Please enter a number')

    except ZeroDivisionError:
        print('Please enter an age greater than 0')

    else:
        print('thank you')
        break

    # runs no matter what
    finally:
        print('ok, i am finally done')
