import random
class Train:
    def __init__(self,trainNo,name,age,gender,typee,fro,to):
        self.trainNo = trainNo
        self.name=name
        self.typee = typee
        self.fro=fro
        self.to = to
        self.age=age
        self.gender=gender
        
    def book(self):
        print(f"Ticket booked for {self.name.title()} {self.age}{self.gender.upper()} in Train no {self.trainNo} from {self.fro.title()} to {self.to.title()}\n")
    
    def berth_and_fare(self):
        if self.typee.upper() == "AC":
            print(f"Your berth no is {random.randint(1,72)} and Coach no is {random.choices(['A', 'B'], k=1)[0]}{random.randint(1,12)}\n")
            print(f"The fare of your journey is ₹{random.randint(1000,3000)}\n")
        elif self.typee.upper() == "SL":
            print(f"Your berth no is {random.randint(1,72)} and Coach no is S{random.randint(1,15)}\n")
            print(f"The fare of your journey is ₹{random.randint(400,800)}\n")
        else:
            print(f"You have booked a Unreserved class so no berth")
            print(f"The fare of your journey is ₹{random.randint(125,350)}\n")
    
    @staticmethod
    def greet():
        print()
        print("Welcome to Indian Railways\n")

    @staticmethod
    def greet1():
        print("Indian Railway wishes You a Happy and Safe journey\n")
    

train_no = int(input("Enter the Train no: "))
namee=input("Enter the name of passenger: ")
age=int(input("Enter the age of passenger: "))
gender = input("Enter the gender in M or F: ")
source=input("Enter the source station: ")
dest = input("Enter the destination station: ")
typee = input("Enter the type of coach you want: ")

passenger = Train(train_no,namee,age,gender,typee,source,dest,)
passenger.greet()
passenger.book()
passenger.berth_and_fare()
passenger.greet1()
