#initializing a class
class employee:
    #special method/ magic method/dunder method - constructor
    def __init__(self):
        print("started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("attributes/data have been initiated")

    def travel(self, destination):   #this needs to call manually
        print("this travel method was called manually")
        print(f"employee is now travelling to {destination}")  

#creating an object/ instance of the class
sam = employee()
#printing the attributes


#print(sam.salary)
#print (sam.id)
sam.travel("kerala") #calling the method
print(type(sam))