#1.- Write a program using classes and objects that:
#Create a person and greet (store the string 'Hello World' in a variable and then display the content of the variable on the screen)

#Program by Omar Ramos Soto ("Trickster-09") on April 13, 2024

class Person():
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(self.name," says: 'Hello World'")
        
persona1 = Person("John")
persona1.greet()