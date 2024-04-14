#3.- Write a program that asks the user for the
#number of hours worked and the hourly rate for each worker.
#Create a method that should display on the screen the corresponding pay.

#Program by Omar Ramos Soto ("Trickster-09") on April 13, 2024

class Worker():
    def __init__(self, name, hourWorked, moneyForHour):
        self.name = name
        self.hourWorked = hourWorked
        self.moneyForHour = moneyForHour
        self.moneyForPay = moneyForHour * hourWorked
        
    
    def showMoneyForPay(self):
        name = input("What's the Worker's name?: ")
        while True :
            hourWorked = int(input("How much hours he worked?: "))
            if hourWorked >= 0 :
                break
        while True:
            moneyForHour = int(input("How much does he earn per hour?: "))
            if moneyForHour >= 0:
                break
        self = Worker(name, hourWorked, moneyForHour)
        print("He earn in total: ",self.moneyForPay,)
        
        
trabajador1 = Worker("", 0,0)
trabajador1.showMoneyForPay()