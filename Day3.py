t1 = ()
t2 =(1,2,3,4)
t3 = 11,22,33
print(t3)
t4 = (11,20.[101,102])
t5 = ((1,2,3),("sun","mon","tue"))

t = (1,2,3,4,5,6,7,8)
# count,index,remove,pop,sort,revrse,append,extend,insert
t1 = [1,2,3]
t2 = [11,22,33]
t1.append(t2)
t1.append([101,102])

# how to delete elements in a tuple 
n = (1,2,3,4)
tt = list(n)
tt.remove(3)
print(tt)

# can you explain how list is mutable and tuple are immutable 
t = [1,2,3,4,5]
t[2] = 111
print(t)
t1 = (1,2,3,4,5)
t1[2] = 111
print(t1)

#set 
s1 = {"sun","mon","tue","wed"}
print(s1)
s1.add("jan")
print(s1)
s1.add("march")
print(s1)

#can u modify
s1.update("ram")
print(s1)

# how to delete 
# dictinoary
d1 = dict()
print(type(d1))

d = {
    "id": 101,
    "name": "ram",
    "age": 22,
    "city": "delhi"
}
print(d)

# convert to list 
keys =[1,2,3,4]
values = ["ram","shyam","mohan","sohan"]
d = dict(zip(keys,values))
print(d)
print(d.keys())
print(d.values())
print(d.items())

#
k = ["id","name","post","salary"]
v = [101,"ram","developer",50000]
d = dict(zip(k,v))
print(d)
print(d["name"])
print(d.get("salary"))

#
d = {
    "id": 101,
    "name": "ram",

}
print(d)
# add 
d["course"] = "python"
print(d)
# update 
d["name"] = "shyam"
print(d)
#remove
d.pop("course")
print(d)

# Implementation of dictinoary mini project 
employee = dict()
while True:
    print("1. Add Employee")
    print("2. View Employee")
    print("3. Search Employee")
    print("4. update Employee")
    print("5. delete Employee")
    print("6. Exit")
choice = int(input("Enter your choice: "))  
if choice == 1:
    id = int(input("Enter employee id: "))
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    city = input("Enter employee city: ")
    employee[id] = {"name": name, "age": age, "city": city}
    print("Employee added successfully!") 
elif choice == 2:
    if not employee:
        print("No employees available.")
    else:
        print("Employees available:")
        for id, details in employee.items():
            print(f"ID: {id}, Name: {details['name']}, Age: {details['age']}, City: {details['city']}")
elif choice == 3:
    search_id = int(input("Enter employee id to search: "))
    if search_id in employee:
        details = employee[search_id]
        print(f"ID: {search_id}, Name: {details['name']}, Age: {details['age']}, City: {details['city']}")
    else:
        print("Employee not found.")
elif choice == 4:
    update_id = int(input("Enter employee id to update: "))
    if update_id in employee:
        name = input("Enter new employee name: ")
        age = int(input("Enter new employee age: "))
        city = input("Enter new employee city: ")
        employee[update_id] = {"name": name, "age": age, "city": city}
        print("Employee updated successfully!")
    else:
        print("Employee not found.")
elif choice == 5:
    delete_id = int(input("Enter employee id to delete: "))
    if delete_id in employee:
        del employee[delete_id]
        print("Employee deleted successfully!")
    else:
        print("Employee not found.")

elif choice == 6:
    print("Exiting the program.")


#product 

# def keyword is used to declared function 
def show():
    print("hello")
show()

#
def sum(a,b):
    print(a+b)
sum(5,10)

# global variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def add():
    print(a+b)
def sub():
    print(a-b)
def multi():
    print(a*b)
def div():
    print(a/b)

# mini project 


cars = {
    "BMW": {
        "model": "X5",
        "price": 8500000,
        "fuel": "Petrol"
    },

    "Audi": {
        "model": "A4",
        "price": 5500000,
        "fuel": "Petrol"
    },

    "Toyota": {
        "model": "Fortuner",
        "price": 4200000,
        "fuel": "Diesel"
    }
}


while True:

    print("\n----- CAR INFORMATION SYSTEM -----")
    print("1. Display Cars")
    print("2. Search Car")
    print("3. Add Car")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # Display cars
    if choice == 1:

        print("\nAvailable Cars:")

        for brand, details in cars.items():
            print("\nBrand:", brand)
            print("Model:", details["model"])
            print("Price:", details["price"])
            print("Fuel:", details["fuel"])


    # Search car
    elif choice == 2:

        brand = input("Enter car brand: ")

        if brand in cars:

            print("\nCar Found!")
            print("Model:", cars[brand]["model"])
            print("Price:", cars[brand]["price"])
            print("Fuel:", cars[brand]["fuel"])

        else:
            print("Car not found!")


    # Add car
    elif choice == 3:

        brand = input("Enter car brand: ")
        model = input("Enter car model: ")
        price = int(input("Enter car price: "))
        fuel = input("Enter fuel type: ")

        cars[brand] = {
            "model": model,
            "price": price,
            "fuel": fuel
        }

        print("Car added successfully!")


    # Exit
    elif choice == 4:

        print("Thank you!")
        break

    else:
        print("Invalid choice!")
