#2.- Write a program that asks the user's name in the console
#and after the user inputs it, display the string Hello <name>!,
#where <name> is the name that the user entered, using objects

#Program by Omar Ramos Soto ("Trickster-09") on April 13, 2024

class Person():
    def __init__(self, name):
        self.name = name
        
    def showName(self):
        nameAux = input("What's your name? ")
        self = Person(nameAux)
        print("Hello",self.name)
        
persona1 = Person("")
persona1.showName()