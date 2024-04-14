#4.- Write a program that asks the user for their weight (in kg) and height (in meters),
#calculates the body mass index and stores it in a variable, and displays the sentence on the screen:
#Your body mass index is <bmi>
#where <bmi> is the calculated body mass index rounded to two decimal places. Using classes and objects.
#Program by Omar Ramos Soto ("Trickster-09") on April 13, 2024

class Person():
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height
        self.IMC = (weight / (height*height))
        
    def ShowIMC(self):
        name = input("What's the person's name? ")
        while True:
            weight = float(input("What's the weight of the person in kg? "))
            if weight >= 0:
                break
        while True:
            height = float(input("What's the height of the person in meters? "))
            if height > 0:
                break
        self = Person(name,weight,height)
        print( "His\her BMI is:", "%.2f" % self.IMC)
        
persona1 = Person("",0,1)
persona1.ShowIMC()