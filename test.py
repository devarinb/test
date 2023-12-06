Q1- Temperature of the city in Fahrenheit is input through the keyboard, write a program to convert this Temperature to Celsius.

Code:

fahrenheit_temp = float(input("Enter temperature in Fahrenheit: "))

celsius_temp = (fahrenheit_temp - 32) * 5/9

print(f"{fahrenheit_temp:.2f} Fahrenheit is equal to {celsius_temp:.2f} Celsius")



Output:

Enter temperature in Fahrenheit: 74

74.00 Fahrenheit is equal to 23.33 Celsius



Q2- Write a python program which accepts basic salary as input and prints the gross salary, which is sum of basic, Dearness allowance (DA) (10% of basic salary) and House Rent Allowance (HRA) (15% of basic allowance).

Code:

basicSalary=float(input("Enter your basic salary "))

dearnessAllowance = .60 * basicSalary

houseRenrAllowance = .15 * basicSalary

grossSalary = (basicSalary + dearnessAllowance + houseRenrAllowance)

print(f"Gross salary is {grossSalary:.2f}")



Output:

Enter your basic salary 15000

Gross salary is 26250.00



Q3- An integer is entered as an input through the keyboard. Write a python program to find out whether it is an odd number or even number.

Code:

number = int(input("Enter an integer: "))

if number % 2 == 0:

print(f"{number} is even.")

else:

print(f"{number} is odd.")



Output:

Enter an integer: 87

87 is odd.



Q4- Write a python program to find maximum and minimum of three number.

Code:

num1 = float(input("Enter first number: "))

num2 = float(input("Enter second number: "))

num3 = float(input("Enter third number: "))

max_num = max(num1, num2, num3)

min_num = min(num1, num2, num3)

print(f"Maximum number: {max_num}")

print(f"Minimum number: {min_num}")



Output:

Enter first number: 45.45

Enter second number: 87

Enter third number: 65.78

Maximum number: 87.0

Minimum number: 45.45



Q5- Write a python program whish accepts 10 integers from the uses and prints them in ascending order.

Code:

numbers = []

for i in range(10):

num = int(input(f"Enter integer {i + 1}: "))

numbers.append(num)

numbers.sort()

print("Numbers in ascending order:", numbers)



Output:

Enter integer 1: 5

Enter integer 2: 9

Enter integer 3: 7

Enter integer 4: 12

Enter integer 5: 8

Enter integer 6: 19

Enter integer 7: 64

Enter integer 8: 89

Enter integer 9: 10

Enter integer 10: 3

Numbers in ascending order: [3, 5, 7, 8, 9, 10, 12, 19, 64, 89]



Q6- Write a python program whish accepts a numbers ‘n’ and print all prime factors of ‘n’.

Code:

def is_prime(num):

if num <= 1:

return False

for i in range(2, int(num ** 0.5) + 1):

if num % i == 0:

return False

return True

def prime_factors(n):

factors = []

divisor = 2

while n > 1:

if n % divisor == 0 and is_prime(divisor):

factors.append(divisor)

n //= divisor

else:

divisor += 1

return factors



# Take input from the user

num = int(input("Enter a number: "))

factors = prime_factors(num)

print(f"Prime factors of {num} are: {factors}")



Output:

Enter a number: 125

Prime factors of 125 are: [5, 5, 5]



Q7- A positive integer is entered through the keyboard, write a python function to find binary equivalent of the numbers using recursion.

Code:

def decimal_to_binary(n):

if n == 0:

return "0"

elif n == 1:

return "1"

else:

return decimal_to_binary(n // 2) + str(n % 2)

# Take input from the user

decimal_num = int(input("Enter an integer: "))

binary_representation = decimal_to_binary(decimal_num)

print(f"The binary representation of {decimal_num} is: {binary_representation}")



Output: 

Enter an integer: 60

The binary representation of 60 is: 111100



















Q1- Write a program create a class employee, where take two object of employee class. Take the attribute employee id, employee name and employee age. Display the two employee details.

Code:

class employee:

    Emp_Name = " "

    Emp_id = 0

    Emp_age = 0

employee1 = employee()

employee2 = employee()

employee1.Emp_Name = "Arindam Biswas"

employee1.Emp_id = 45

employee1.Emp_age = 25

employee2.Emp_Name = "Suresh"

employee2.Emp_id = 49

employee2.Emp_age = 24

print("Name: ", employee1.Emp_Name)

print("Id: ", employee1.Emp_id)

print("Age: ", employee1.Emp_age)

print("Name: ", employee2.Emp_Name)

print("Id: ", employee2.Emp_id)

print("Age: ", employee2.Emp_age)



Output:

Name:  Arindam Biswas

Id:  45

Age:  25

Name:  Suresh

Id:  49

Age:  24



Q2- Write a class room. Take two attribute length and breath. Take a method calculate area. In the method calculate room area.

Code: 

class room():

    def __init__(self, breadth, length):

        self.breadth = breadth

        self.length = length



    def area(self):

        return self.breadth * self.length



# Input valus

a = int(input("Enter length of room: "))

b = int(input("Enter breadth of room: "))

obj = room(a, b)

print("Area of room:", obj.area())

print()



Output:

Enter length of room: 80

Enter breadth of room: 45

Area of room: 3600

Q3- Write a python program to create a calculator class. Include method for basic arithmetic operation.

Code:

class Calculator:

    def add(self, num1, num2):

        return num1 + num2

    def subtract(self, num1, num2):

        return num1 - num2

    def multiply(self, num1, num2):

        return num1 * num2

    def divide(self, num1, num2):

        if num2 != 0:

            return num1 / num2

        else:

            return "Cannot divide by zero"



# Creating an instance of the Calculator class

calculator = Calculator()

result_add = calculator.add(5, 3)

result_subtract = calculator.subtract(10, 4)

result_multiply = calculator.multiply(2, 6)

result_divide = calculator.divide(8, 2)



# Displaying results

print(f"Addition: {result_add}")

print(f"Subtraction: {result_subtract}")

print(f"Multiplication: {result_multiply}")

print(f"Division: {result_divide}")



Output:

Addition: 8

Subtraction: 6

Multiplication: 12

Division: 4.0

























Q1- Create a class, Person. Take a default constructor where take attributes name and age. Display all the details of Person.

Code:

class Person:

    def __init__(self):

        self.name="Arindam Biswas"

        self.age=25

P=Person()

#print the values of attributes

print("Name: ",P.name,"\n","Age: ",P.age)



Output:

Name:  Arindam Biswas 

 Age:  25



Q2- Create a class, Person. Take a parameterized constructor where take arguments name and age. Display all details of Person.

Code:

class Person:

    def __init__(self,name,age):

        self.name=name

        self.age=age

P=Person("Arindam Biswas",25)

#print the values of attributes

print("Name: ",P.name)

print("Age : ",P.age)



Output:

Name:  Arindam Biswas

Age :  25



Q3- Create a python class Student. Take argument-name, age and roll-on. Display details about Student through parameterized.

Code:

class Student:    

    def __init__(self,name,age,rollno):

        self.name=name

        self.age=age

        self.rollno=rollno

P=Student("Arindam Biswas", 25, 10000222034)

print("Name: ",P.name)

print("Age : ",P.age)

print("Roll No.: ",P.rollno)



Output:

Name:  Arindam Biswas

Age :  25

Roll No.:  10000222034



Q4- Create a python class Student. Take argument-name, age and roll-no. Display details about Student through parameterized constructor. Use the built-in function of class structure.

Code: 

class Student:

    def __init__(self,name,age,rollno):

        self.name=name

        self.age=age

        self.rollno=rollno

S = Student("Arindam Biswas", 25, 10000222034)



#print the values of attributes

print("Name: ",S.name)

print("Age :",S.age)

print("Roll No.: ",S.rollno)

#Using the built-in function of class structure

i=getattr(S,"name")

print(i)

setattr(S,'age',23)

j=getattr(S,'age',)

print(j)



k=hasattr(S,"rollno")

print(k)

delattr(S,'rollno')

i=hasattr(S,"rollno")

print(i)



Output:

Name:  Arindam Biswas

Age : 25

Roll No.:  10000222034

Arindam Biswas

23

True

False

















Q1- Write two or three parameter addition using method overloading.

Code:

class Add:

    def sum(self, a=None, b=None, c=None):

        if a != None and b != None and c != None:

            print("Addition of Three parameter: ", a + b + c)

        elif a != None and b != None:

            print("Addition of two parameter: ", a + b)

        else:

            print("Please enter sum input!")

# create object

o1 = Add()

o1.sum(6, 10)

o1.sum(6, 10, 8)

o1.sum()



Output: 

Addition of two parameter:  16

Addition of Three parameter:  24

Please enter sum input!



Q2- Write a class compute where compute area of rectangle or square by using method overloading.

Code:

class area:

    def find_area(self, a=None, b= None):

        if a is not None and b is not None:

            print ("Area of Rectangle:",a*b)

        elif a is not None:

            print("Area of Square:",a*a)

        else:

            print("No Input")



#create objects

area1=area()

area1.find_area(12,7)

area1.find_area(5)

area1.find_area() 



Output:

Area of Rectangle: 84

Area of Square: 25

No Input



Q3- Write a class compute tow ‘int’ addition and two ‘string’ addition by using overloading

Code:

class operator:

    def __init__(self, a):

        self.a = a

    def __add__(self, b):

        return self.a + b.a

#create object

object1 = operator(1)

object2 = operator(2)

object3 = operator("Hello ")

object4 = operator("Arindam")



print(object1 + object2)

print(object3 + object4)



Output:

3

Hello Arindam



Q4- Write a python program addition of two complex number using binary+ overloading.

Code:

class ComplexNumber:

    def __init__(self, real, imag):

        self.real = real

        self.imag = imag



    def __add__(self, other):

        # Overloading the + operator for complex number addition

        new_real = self.real + other.real

        new_imag = self.imag + other.imag

        return ComplexNumber(new_real, new_imag)



    def __str__(self):

        # Overriding the __str__ method for a better string representation

        return f"{self.real} + {self.imag}j"

complex1 = ComplexNumber(2, 3)

complex2 = ComplexNumber(1, 4)

result_complex = complex1 + complex2

print(f"Result of Addition: {result_complex}")



Output: 

Result of Addition: 3 + 7j



















Q1- Bank Account Inheritance: Design a class hierarchy for different types of bank accounts, such as savings accounts, checking accounts, and fixed deposit accounts. Implement common operations like deposits, withdrawals, and balance inquiries, and then extend the classes to handle specific account types with different interest rates and rules.

Code:

class BankAccount:

    def __init__(self, account_number, holder_name, balance=0):

        self.account_number = account_number

        self.holder_name = holder_name

        self.balance = balance



    def deposit(self, amount):

        if amount > 0:

            self.balance += amount

            return True

        else:

            return False



    def withdraw(self, amount):

        if amount > 0 and amount <= self.balance:

            self.balance -= amount

            return True

        else:

            return False



    def get_balance(self):

        return self.balance





class SavingsAccount(BankAccount):

    def __init__(self, account_number, holder_name, balance=0, interest_rate=0.02):

        super().__init__(account_number, holder_name, balance)

        self.interest_rate = interest_rate



    def calculate_interest(self):

        return self.balance * self.interest_rate





class CheckingAccount(BankAccount):

    def __init__(self, account_number, holder_name, balance=0, overdraft_limit=1000):

        super().__init__(account_number, holder_name, balance)

        self.overdraft_limit = overdraft_limit



    def withdraw(self, amount):

        if amount <= self.balance + self.overdraft_limit:

            self.balance -= amount

            return True

        else:

            return False





class FixedDepositAccount(BankAccount):

    def __init__(self, account_number, holder_name, balance=0, interest_rate=0.05, term_months=12):

        super().__init__(account_number, holder_name, balance)

        self.interest_rate = interest_rate

        self.term_months = term_months



    def calculate_interest(self):

        return self.balance * self.interest_rate * (self.term_months / 12)





# Example usage:

savings_account = SavingsAccount("SA123", "Manu Singh")

savings_account.deposit(1000)

savings_account.calculate_interest()



checking_account = CheckingAccount("CA456", "Arit Sen")

checking_account.deposit(500)

checking_account.withdraw(800)



fd_account = FixedDepositAccount("FD789", "Sambhu Saha")

fd_account.deposit(10000)

fd_account.calculate_interest()



Q2- Define a base class "Employee" and create derived classes for different job roles (e.g., "Manager," "Technician," "HR"). Include attributes like "name," "employee_id" and role-specific methods for managing employee tasks.

Code:

class Employee:

    def __init__(self, name, employee_id):

        self.name = name

        self.employee_id = employee_id



    def display_info(self):

        print(f"Name: {self.name}")

        print(f"Employee ID: {self.employee_id}")





class Manager(Employee):

    def __init__(self, name, employee_id, department):

        super().__init__(name, employee_id)

        self.department = department

        self.managed_employees = []



    def add_employee(self, employee):

        self.managed_employees.append(employee)



    def display_managed_employees(self):

        print(f"Managed Employees for Manager {self.name}:")

        for employee in self.managed_employees:

            print(f"- {employee.name}")





class Technician(Employee):

    def __init__(self, name, employee_id, skills):

        super().__init__(name, employee_id)

        self.skills = skills



    def display_skills(self):

        print(f"Skills of Technician {self.name}:")

        for skill in self.skills:

            print(f"- {skill}")





class HR(Employee):

    def __init__(self, name, employee_id, responsibilities):

        super().__init__(name, employee_id)

        self.responsibilities = responsibilities



    def display_responsibilities(self):

        print(f"HR Responsibilities for {self.name}:")

        for responsibility in self.responsibilities:

            print(f"- {responsibility}")





# Example usage:

print("============")

manager = Manager("Arindam Biswas", "M01", "Sales")

manager.add_employee(Employee("Souvik Mondal", "R01"))

manager.add_employee(Employee("Sautik Pal", "B01"))

manager.display_info()

manager.display_managed_employees()

print("============")

technician = Technician("Aparna Sen", "D01", ["Networking", "Hardware"])

technician.display_info()

technician.display_skills()

print("============")

hr = HR("Ankush Karmakar", "M03", ["Recruitment", "Employee Hire"])

hr.display_info()

hr.display_responsibilities()

print("============")



Output:

============

Name: Arindam Biswas

Employee ID: M01

Managed Employees for Manager Arindam Biswas:

- Souvik Mondal

- Sautik Pal

============

Name: Aparna Sen

Employee ID: D01

Skills of Technician Aparna Sen:

- Networking

- Hardware

============

Name: Ankush Karmakar

Employee ID: M03

HR Responsibilities for Ankush Karmakar:

- Recruitment

- Employee Hire

============







Q3-  Library Catalog System: Develop a library catalog system with a base class "Library Item" and derived classes for different item types (e.g., "Book," "DVD," "Magazine"). Include attributes like "title," "author," and "checkout_status." Use inheritance to manage common library operations like checking out and returning items.

Code: 

class LibraryItem:

    def __init__(self, title, author):

        self.title = title

        self.author = author

        self.checkout_status = False



    def checkout(self):

        if not self.checkout_status:

            self.checkout_status = True

            return f"{self.title} by {self.author} has been checked out."

        else:

            return f"{self.title} by {self.author} is already checked out."



    def return_item(self):

        if self.checkout_status:

            self.checkout_status = False

            return f"{self.title} by {self.author} has been returned."

        else:

            return f"{self.title} by {self.author} is not checked out."





class Book(LibraryItem):

    def __init__(self, title, author, isbn):

        super().__init__(title, author)

        self.isbn = isbn



    def get_info(self):

        return f"Book Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}"





class DVD(LibraryItem):

    def __init__(self, title, director, duration):

        super().__init__(title, director)

        self.director = director

        self.duration = duration



    def get_info(self):

        return f"DVD Title: {self.title}\nDirector: {self.director}\nDuration: {self.duration} minutes"





class Magazine(LibraryItem):

    def __init__(self, title, publisher, issue_number):

        super().__init__(title, publisher)

        self.publisher = publisher

        self.issue_number = issue_number



    def get_info(self):

        return f"Magazine Title: {self.title}\nPublisher: {self.publisher}\nIssue Number: {self.issue_number}"





# Example usage:

book = Book("DATA STRUCTURES", "Lipschutz", "978-1-25-902996-7")

dvd = DVD("Guardian of The Galaxy Vol-3", "Anthony Russo and Joe Russo", 182)

magazine = Magazine("National Geographic", "National Geographic Society", 202)



print(book.checkout())

print(dvd.checkout())

print(magazine.checkout())

print(book.return_item())

print(dvd.return_item())

print(magazine.return_item())

print(book.get_info())

print(dvd.get_info())

print(magazine.get_info())



Output:

DATA STRUCTURES by Lipschutz has been checked out.

Guardian of The Galaxy Vol-3 by Anthony Russo and Joe Russo has been checked out.

National Geographic by National Geographic Society has been checked out.

DATA STRUCTURES by Lipschutz has been returned.

Guardian of The Galaxy Vol-3 by Anthony Russo and Joe Russo has been returned.

National Geographic by National Geographic Society has been returned.

Book Title: DATA STRUCTURES

Author: Lipschutz

ISBN: 978-1-25-902996-7

DVD Title: Guardian of The Galaxy Vol-3

Director: Anthony Russo and Joe Russo

Duration: 182 minutes

Magazine Title: National Geographic

Publisher: National Geographic Society

Issue Number: 202



Q4- Shape Sorting with Inheritance: Implement a program that creates a list of various shapes (e.g., circles, rectangles, triangles) and sorts them based on their areas using inheritance. Each shape should have a method to calculate its area, and you should use inheritance to create specialized shape classes.

Code:

import math

class Shape:

    def area(self):

        pass

class Circle(Shape):

    def __init__(self, radius):

        self.radius = radius



    def area(self):

        return math.pi * self.radius ** 2

class Rectangle(Shape):

    def __init__(self, width, height):

        self.width = width

        self.height = height



    def area(self):

        return self.width * self.height

class Triangle(Shape):

    def __init__(self, base, height):

        self.base = base

        self.height = height



    def area(self):

        return 0.5 * self.base * self.height

shapes = [

    Circle(2),

    Rectangle(6, 9),

    Triangle(10, 8),

]

shapes.sort(key=lambda x: x.area())

for shape in shapes:

    print(f"Shape: {type(shape).__name__}, Area: {shape.area():.2f}")



Output:

Shape: Circle, Area: 12.57

Shape: Triangle, Area: 40.00

Shape: Rectangle, Area: 54.00



Q5- Online Shopping Cart: Create an online shopping cart system using inheritance. Design a base class "Product" and derived classes for various product categories (e.g., "Electronics," "Clothing," "Books"). Implement methods for adding/removing items from the cart and calculating the total price with appropriate discounts for each category.

Code:

class Product:

    def __init__(self, name, price):

        self.name = name

        self.price = price



    def calculate_discount(self):

        # Base class method for calculating discount

        return 0



class ElectronicsProduct(Product):

    def __init__(self, name, price, warranty_period):

        super().__init__(name, price)

        self.warranty_period = warranty_period



    def calculate_discount(self):

        # Apply a 10% discount for electronics products

        return 0.1 * self.price



class ClothingProduct(Product):

    def __init__(self, name, price, size):

        super().__init__(name, price)

        self.size = size



    def calculate_discount(self):

        # Apply a 5% discount for clothing products

        return 0.05 * self.price



class BooksProduct(Product):

    def __init__(self, name, price, author):

        super().__init__(name, price)

        self.author = author



    def calculate_discount(self):

        # Apply a 15% discount for books products

        return 0.15 * self.price



class ShoppingCart:

    def __init__(self):

        self.items = []



    def add_item(self, product):

        self.items.append(product)

        print(f"Added {product.name} to the cart.")



    def remove_item(self, product):

        if product in self.items:

            self.items.remove(product)

            print(f"Removed {product.name} from the cart.")

        else:

            print(f"{product.name} not found in the cart.")



    def calculate_total_price(self):

        total_price = sum(product.price - product.calculate_discount() for product in self.items)

        return total_price



# Example usage

electronics_product = ElectronicsProduct("Laptop", 1000, "2 years")

clothing_product = ClothingProduct("T-shirt", 20, "Large")

books_product = BooksProduct("Python Programming", 50, "John Doe")



shopping_cart = ShoppingCart()



shopping_cart.add_item(electronics_product)

shopping_cart.add_item(clothing_product)

shopping_cart.add_item(books_product)



print("Total Price:", shopping_cart.calculate_total_price())



Output:

Added Laptop to the cart.

Added T-shirt to the cart.

Added Python Programming to the cart.

Total Price: 961.5

















Q1- Create a base class called "Shape" with a method calculate_area() that returns 0. Then, create derived classes for different shapes like "Circle," "Rectangle," and "Triangle." Override the calculate_area() method in each derived class to calculate and return the area of that specific shape.

Code:

import math



class Shape:

    def calculate_area(self):

        return 0



class Circle(Shape):

    def __init__(self, radius):

        self.radius = radius



    def calculate_area(self):

        return math.pi * self.radius ** 2



class Rectangle(Shape):

    def __init__(self, length, width):

        self.length = length

        self.width = width



    def calculate_area(self):

        return self.length * self.width



class Triangle(Shape):

    def __init__(self, base, height):

        self.base = base

        self.height = height



    def calculate_area(self):

        return 0.5 * self.base * self.height



# Example usage

circle = Circle(radius=5)

rectangle = Rectangle(length=4, width=6)

triangle = Triangle(base=3, height=8)



print(f"Area of Circle: {circle.calculate_area()}")

print(f"Area of Rectangle: {rectangle.calculate_area()}")

print(f"Area of Triangle: {triangle.calculate_area()}")



Output:

Area of Circle: 78.53981633974483

Area of Rectangle: 24

Area of Triangle: 12.0













Q2- Create an abstract class "PaymentGateway" with abstract methods for payment-related operations like process_payment() and refund_payment(). Create concrete subclasses for different payment gateways (e.g., "PayPal," "Stripe") and implement these methods to interact with the respective payment systems.

Code:

from abc import ABC, abstractmethod



class PaymentGateway(ABC):

    @abstractmethod

    def process_payment(self, amount):

        pass



    @abstractmethod

    def refund_payment(self, transaction_id):

        pass



class PayPal(PaymentGateway):

    def process_payment(self, amount):

        print(f"Processing PayPal payment of ${amount}")

        # Include PayPal-specific implementation for processing payment

        transaction_id = "PP123456"

        return transaction_id



    def refund_payment(self, transaction_id):

        print(f"Refunding PayPal payment for transaction ID: {transaction_id}")

        # Include PayPal-specific implementation for refunding payment



class Stripe(PaymentGateway):

    def process_payment(self, amount):

        print(f"Processing Stripe payment of ${amount}")

        # Include Stripe-specific implementation for processing payment

        transaction_id = "ST789012"

        return transaction_id



    def refund_payment(self, transaction_id):

        print(f"Refunding Stripe payment for transaction ID: {transaction_id}")

        # Include Stripe-specific implementation for refunding payment



# Example usage

paypal_gateway = PayPal()

stripe_gateway = Stripe()



# Process payments

paypal_transaction_id = paypal_gateway.process_payment(50)

stripe_transaction_id = stripe_gateway.process_payment(75)



# Refund payments

paypal_gateway.refund_payment(paypal_transaction_id)

stripe_gateway.refund_payment(stripe_transaction_id)



Output:

Processing PayPal payment of $50

Processing Stripe payment of $75

Refunding PayPal payment for transaction ID: PP123456

Refunding Stripe payment for transaction ID: ST789012





Q1- Write a program for Division by zero Exception Handling.

Code:

def divide_numbers(dividend, divisor):

    try:

        result = dividend / divisor

        print(f"Result of division: {result}")

    except ZeroDivisionError:

        print("Error: Division by zero is not allowed.")

    except Exception as e:

        print(f"An unexpected error occurred: {e}")

    finally:

        print("Division operation completed.")



# Example usage

num1 = 10

num2 = 0



divide_numbers(num1, num2)



Output: 

Error: Division by zero is not allowed.

Division operation completed.



Q2- Take a user-defined array and display it. Do exception handling, if array index out ofbound otherwise execute code when there is no error.

Code:

def display_array_element(arr, index):

    try:

        element = arr[index]

        print(f"Element at index {index}: {element}")

    except IndexError:

        print("Error: Array index out of bounds. Please provide a valid index.")

    except Exception as e:

        print(f"An unexpected error occurred: {e}")

    else:

        print("Code execution when there is no error.")



# Example usage

try:

    # Taking a user-defined array

    user_array = [int(x) for x in input("Enter elements of the array (space-separated): ").split()]



    # Taking user input for the index

    user_index = int(input("Enter the index to display: "))



    # Calling the function to display the array element

    display_array_element(user_array, user_index)



except ValueError:

    print("Error: Please enter valid numerical values for array elements and index.")

except Exception as e:

    print(f"An unexpected error occurred: {e}")

finally:

    print("Program execution completed.")



Output:

Enter elements of the array (space-separated): 45 87 18 65 84 50 

Enter the index to display: 6

Error: Array index out of bounds. Please provide a valid index.

Program execution completed.

























































Q1- Design a student registration form.

Code:

import tkinter as tk





def submit_form():

    name = name_entry.get()

    age = age_entry.get()

    gender = gender_var.get()



    print("Name:",name,"\nAge:",age,"\nGender:",gender)





# Create the main window

window = tk.Tk()

window.title("Student Registration Form")



# Create and place labels, entry widgets, and radio buttons

tk.Label(window, text="Name:").pack(pady=5)

name_entry = tk.Entry(window)

name_entry.pack(pady=5)



tk.Label(window, text="Age:").pack(pady=5)

age_entry = tk.Entry(window)

age_entry.pack(pady=5)



tk.Label(window, text="Gender:").pack(pady=5)

gender_var = tk.StringVar()

gender_var.set("Male")  # Default selection

tk.Radiobutton(window, text="Male", variable=gender_var, value="Male").pack()

tk.Radiobutton(window, text="Female", variable=gender_var, value="Female").pack()



# Create and place the submit button

submit_button = tk.Button(window, text="Submit", command=submit_form)

submit_button.pack(pady=10)



# Start the Tkinter event loop

window.mainloop()



Output:

  

Name: Arindam Biswas 

Age: 25 

Gender: Male

Q2- Design a user login page.

Code:

import tkinter as tk



def authenticate():

    entered_username = username_entry.get()

    entered_password = password_entry.get()



    if entered_username == "admin" and entered_password == "password":

        result_label.config(text="Login Successful", fg="green")

    else:

        result_label.config(text="Login Failed. Please try again.", fg="red")



# Create the main window

window = tk.Tk()

window.title("User Login")



# Create and place labels, entry widgets, and result label

tk.Label(window, text="Username:").pack(pady=5)

username_entry = tk.Entry(window)

username_entry.pack(pady=5)



tk.Label(window, text="Password:").pack(pady=5)

password_entry = tk.Entry(window, show="*")

password_entry.pack(pady=5)



submit_button = tk.Button(window, text="Login", command=authenticate)

submit_button.pack(pady=10)



result_label = tk.Label(window, text="")

result_label.pack()



# Start the Tkinter event loop

window.mainloop()



Output:

 

