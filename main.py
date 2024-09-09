class Employee:

    def __init__(self):
        print("Employee created")
    

    def __del__(self):
        print("employee deleted")




employee1 = Employee()
del employee1
