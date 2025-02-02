# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': True
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid'] == True:
            result = fn(*args, **kwargs)
        else:
            return print("user not valid")
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
