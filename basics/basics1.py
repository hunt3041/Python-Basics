# OOP
class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def shout(self):
        print(f'My name is {self.name}')

    @classmethod
    # cls is dummy variabl that allows method to be used without instantiating object
    def adding_things(cls, num1, num2):
        return num1 + num2
    
    @staticmethod
    def adding_things(num1, num2):
        return num1 + num2
        

player1 = PlayerCharacter("Hunter", 22)
player2 = PlayerCharacter("Tom", 45)

string1 = "hello"

"hello".age = 12

print("hello".age)

