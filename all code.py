#!/usr/bin/env python
# coding: utf-8

# # 1. square of first 5 no:

# In[14]:



def su(n):
    s1=0
    pr=0
    for i in range(0,n):
        s1=(s1+i+pr)
        pr=i
        print(s1)
n=6
su(n)


# In[6]:


def Psquare(n):
    sum1=0
    pr=0
    for i in range(0, n):
        sum1 = (sum1+i+pr)
        print(sum1,end=" ")
        pr=i
n=5
Psquare(n)


# In[12]:


# Python Exercise: Generate and print a list where the values are square of numbers between two numbers
def printValues():
    l = list()
    for i in range(1,21):
        l.append(i**2)
    print(l)
    
printValues()


# # 2. Python Program for Sum of squares of first n natural numbers
# Input : N = 4
# Output : 30
# 12 + 22 + 32 + 42
# = 1 + 4 + 9 + 16
# = 30

# In[15]:


def sumofsquare(n):
    s2=0
    for i in range(0,n+1):
        s2=s2+(i*i)
    return s2
n=6
sumofsquare(n)


# # 3. python prgram for maximum no in list

# In[17]:


l1=[1,2,5,8,8,9,0,10,99]
print(max(l1))


# # 4. python program 2nd highest number

# In[21]:


l1=[1,2,5,8,8,9,0,10,99]
l1.sort()
print(l1[-2])


# In[22]:


list1 = [10, 20, 4, 45, 99]
new_list = set(list1)
new_list.remove(max(new_list))
print(max(new_list))


# # 5. python program for reverse order of list

# In[29]:


l2=[1,5,6,7,1,8,9,10,11]
l3=[44,55,77,88]
l2.extend(l3)
print(l2)


# In[30]:


a1 = [1, 2]
a2 = [1, 2]
b = (3, 4)

# a1 = [1, 2, 3, 4]
a1.extend(b) 
print(a1)

# a2 = [1, 2, (3, 4)]
a2.append(b)
print(a2)


# # 6. python remove duplicate number

# In[31]:


test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print ("The original list is : " +  str(test_list))
  
# using naive method
# to remove duplicated 
# from list 
res = []
for i in test_list:
    if i not in res:
        res.append(i)
  
# printing list after removal 
print ("The list after removing duplicates : " + str(res))


# # 7. python remove duplicate no in list compression

# In[32]:


# initializing list
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print ("The original list is : " +  str(test_list))
  

res = []
[res.append(x) for x in test_list if x not in res]
  
# printing list after removal 
print ("The list after removing duplicates : " + str(res))


# In[33]:


mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)


# In[34]:


test_list = [1, 3, 4, 5]
  
# initialize string 
test_str = 'gfg'
  
# printing original list 
print("The original list : " + str(test_list))
  
# printing original string 
print("The original string : " + str(test_str))
  
# Appending String to list
# using append()
test_list.append(test_str)
  
# printing result
print("The list after appending is : " + str(test_list))


# # 8. python even and odd

# In[35]:


num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))


# In[11]:


# Python program to print odd Numbers in given range

start, end = 4, 19

# iterating each number in list
for num in range(start, end + 1):
    # checking condition
    if num % 2 != 0:
        print(num, end = " ")


# In[36]:


year = int(input("Enter a year: "))  
if (year % 4) == 0:  
   if (year % 100) == 0:  
       if (year % 400) == 0:  
           print("{0} is a leap year".format(year))  
       else:  
           print("{0} is not a leap year".format(year))  
   else:  
       print("{0} is a leap year".format(year))  
else:  
   print("{0} is not a leap year".format(year))  



# # 9. how to create list without inbuilt function

# In[10]:


# inbuilt function
l1=[]
print(l1)
l1.append(1)
l1.append(2)
l1.append(3)
print(l1)

# without inbult function
l2=[]
print(l2)
for i in range(1,8):
    l2.append(i)
print(l2)

# or without inbuilt function
l3=[]
print(l3)
l3.append((5,9))
print(l3)

# or string added
l4=[]
l5=['for in the list','i love india']
l4.append(l5)
print(l4)


# # 10. python code for factorized

# In[21]:


# recurssive fatorized method
def fact(n):  
    return 1 if (n==1 or n==0) else n * fact(n - 1);  
  
num = 5  
print("Factorial of",num,"is",)  
fact(num) 


# In[24]:


# without recurssive function
n=int(input("enter a factorized: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)


# In[23]:


# Python 3 program to find factorial of given number inbuilt function
import math

def factorial(n):
    return(math.factorial(n))


# Driver Code
num = 5
print("Factorial of", num, "is",factorial(num))


# # 11. python code for multiplication table

# In[13]:


num = int(input("Enter the number: "))

print("Multiplication Table of", num)
for i in range(1, 11):
   print(num,"X",i,"=",num * i)


# In[14]:


for i in range(1,11):
    print("\n\nMULTIPLICATION TABLE FOR %d\n" %(i))
    for j in range(1,11):
        print("%-5d X %5d = %5d" % (i, j, i*j))


# # 12. python code for prime number

# In[38]:


# Python program to display all the prime numbers within an interval

lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


# In[40]:


# Python program to print all
# prime number in an interval
# number should be greater than 1
start = 11
end = 25

for i in range(start, end+1):
    if i>1:
        for j in range(2,i):
            if(i % j==0):
                break
        else:
            print(i)


# # 13. python code for fibonacci sequence
# A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....
# 
# The first two terms are 0 and 1. All other terms are obtained by adding the preceding two terms. This means to say the nth term is the sum of (n-1)th and (n-2)th term.

# In[36]:


# Function for nth Fibonacci number
def Fibonacci(n):
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

# Driver Program
print(Fibonacci(9))


# In[37]:


# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1


# # 14. python code for polynomorphism

# In[46]:


'''
Example 1: Polymorphism in addition operator
We know that the + operator is used extensively in Python programs. But, it does not have a single usage.

For integer data types, + operator is used to perform arithmetic addition operation.
'''
num1 = 1
num2 = 2
print(num1+num2)

# Similarly, for string data types, + operator is used to perform concatenation.

str1 = "Python"
str2 = "Programming"
print(str1+" "+str2)

# A simple Python function to demonstrate
# Polymorphism

def add(x, y, z = 0):
    return x + y+z

# Driver code
print(add(2, 3))
print(add(2, 3, 4))


# In[43]:


'''
Function Polymorphism in Python
There are some functions in Python which are compatible to run with multiple data types.

One such function is the len() function. It can run with many data types in Python. Let's look at some example use cases of the function.

Example 2: Polymorphic len() function
'''

print(len("Programiz"))
print(len(["Python", "Java", "C"]))
print(len({"Name": "John", "Address": "Nepal"}))


# In[44]:


'''
Class Polymorphism in Python
Polymorphism is a very important concept in Object-Oriented Programming.


To learn more about OOP in Python, visit: Python Object-Oriented Programming

We can use the concept of polymorphism while creating class methods as Python allows different classes to have methods with the same name.

We can then later generalize calling these methods by disregarding the object we are working with. Let's look at an example:

Example 3: Polymorphism in Class Methods
'''    
    
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()


# In[47]:


# polymorphism of class method

class India():
    def capital(self):
        print("New Delhi is the capital of India.")
    def language(self):
        print("Hindi is the most widely spoken language of India.")
    def type(self):
        print("India is a developing country.")

class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
    def language(self):
        print("English is the primary language of USA.")
    def type(self):
        print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()


# In[45]:


'''
Polymorphism and Inheritance
Like in other programming languages, the child classes in Python also inherit methods and attributes from the parent class. We can redefine certain methods and attributes specifically to fit the child class, which is known as Method Overriding.

Polymorphism allows us to access these overridden methods and attributes that have the same name as the parent class.

Let's look at an example:

Example 4: Method Overriding
'''

from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2


a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())


# In[48]:


'''
Polymorphism with a Function and objects:
It is also possible to create a function that can take any object, allowing for polymorphism. 
In this example, let’s create a function called “func()” 
which will take an object which we will name “obj”. Though we are using the name ‘obj’, any instantiated object will be able to be called into this function. Next, lets give the function something to do that uses the ‘obj’ object we passed to it. In this case lets call the three methods, viz., capital(), language() and type(), each of which is defined in the two classes ‘India’ and ‘USA’. Next, let’s create instantiations of both the ‘India’ and ‘USA’ classes if we don’t have them already. With those, we can call their action using the same func() function:
'''

class India():
    def capital(self):
        print("New Delhi is the capital of India.")
    def language(self):
        print("Hindi is the most widely spoken language of India.")
    def type(self):
        print("India is a developing country.")

class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
    def language(self):
        print("English is the primary language of USA.")
    def type(self):
        print("USA is a developed country.")

def func(obj):
    obj.capital()
    obj.language()
    obj.type()

obj_ind = India()
obj_usa = USA()

func(obj_ind)
func(obj_usa)


# # 15. python code for inheritence

# In[51]:


# Python code to demonstrate how parent constructors
# are called.

# parent class
class Person( object ):
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

# child class
class Employee( Person ):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
        
# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")	

# calling a function of the class Person using its instance
a.display()


# # 16. python code for check your mobile no and email address is valid or not
# 
# 1. Mobile Number validation criteria:
# 
# The first digit should contain number between 7 to 9.
# The rest 9 digit can contain any number between 0 to 9.
# The mobile number can have 11 digits also by including 0 at the starting.
# The mobile number can be of 12 digits also by including 91 at the starting
# The number which satisfies the above criteria, is a valid mobile Number. 
# Examples:
# 
# Input : Enter Mobile Number:
#         7873923408
# Output :Valid Mobile Number
# 
# Input : Enter Mobile Number:
#         5678729234
# Output :Invalid Mobile Number
# Prerequisites : Java Regular Expressions
# 
# 
# 2. Email id is valid or not 
# rerequisite: Regex in Python
# Given a string, write a Python program to check if the string is a valid email address or not. 
# An email is a string (a subset of ASCII characters) separated into two parts by @ symbol, a “personal_info” and a domain, that is personal_info@domain.
# Examples: 
# 
# Input:  ankitrai326@gmail.com
# Output: Valid Email
# 
# Input: my.ownsite@ourearth.org
# Output: Valid Email
# 
# Input: ankitrai326.com
# Output: Invalid Email 
# In this program, we are using search() method of re module. so let’s see the description about it.
# re.search() : This method either returns None (if the pattern doesn’t match), or re.MatchObject that contains information about the matching part of the string. This method stops after the first match, so this is best suited for testing a regular expression more than extracting data. 
# Let’s see the Python program to validate an Email : 
# 
# 

# In[55]:


# 1. Mobile Number validation criteria:

# Python program to check if
# given mobile number is valid
import re

def isValid(s):
    # 1) Begins with 0 or 91
    # 2) Then contains 7 or 8 or 9.
    # 3) Then contains 9 digits
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
    return Pattern.match(s)

# Driver Code
s = "347873923408"
if (isValid(s)):
    print ("Valid Number")
else :
    print ("Invalid Number")


# This code is contributed by rishabh_jain


# In[61]:


# 2. Email id is valid or not 

# Python program to validate an Email

# import re module

# re module provides support
# for regular expressions
import re

# Make a regular expression
# for validating an Email
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

# Define a function for
# for validating an Email


def check(email):
    # pass the regular expression and the string in search() method
    if(re.search(regex, email)):
        print("Valid Email")
    else:
        print("Invalid Email")


# Driver Code
if __name__ == '__main__':
    # Enter the email
    email = "ankitrai326@gmail.com"
    # calling run function
    check(email)
    email = "my.ownsite@our-earth.org"
    check(email)
    email = "ankitrai326.com"
    check(email)


# # 17. python code for count double word and number count

# In[29]:


some_list=['a','b','c','b','d','m','n','n']

my_list=sorted(some_list)
 
duplicates=[]
for i in my_list:
     if my_list.count(i)>1:
         if i not in duplicates:
             duplicates.append(i)
 
print(duplicates)


# In[32]:


MyList = ["a", "b", "a", "c", "c", "a", "c"]

my_dict = {i:MyList.count(i) for i in MyList}
print(my_dict)

MyList = ["b", "a", "a", "c", "b", "a", "c",'a']
duplicate_dict = {i:MyList.count(i) for i in MyList}
print(duplicate_dict)


# In[33]:


#we need to import counter function.
from collections import Counter
MyList = ["a", "b", "a", "c", "c", "a", "c"]
duplicate_dict = Counter(MyList)
print(duplicate_dict)#to get occurence of each of the element.
print(duplicate_dict['a'])# to get occurence of specific element.


# In[34]:


MyList = ["b", "a", "a", "c", "b", "a", "c",'a']
counter_b=MyList.count('b')
print(counter_b)


# In[35]:


# without inbuilt function
MyList = ["b", "a", "a", "c", "b", "a", "c",'a']
count=0
for i in MyList:
    if i == 'a': 
        count = count + 1  
print ("the number of a in MyList is :", count)


# # 18. python code for armstrong number
# A number is called Armstrong number if it is equal to the sum of the cubes of its own digits.
# 
# For example: 153 is an Armstrong number since 153 = 1*1*1 + 5*5*5 + 3*3*3.

# In[26]:


num = int(input("Enter a number: "))  
sum = 0  
temp = num  
  
while temp > 0:  
   digit = temp % 10  
   sum += digit ** 3  
   temp //= 10  
  
if num == sum:  
   print(num,"is an Armstrong number")  
else:  
   print(num,"is not an Armstrong number")


# In[27]:


lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
  
for num in range(lower,upper + 1):  
   sum = 0  
   temp = num  
   while temp > 0:  
       digit = temp % 10  
       sum += digit ** 3  
       temp //= 10  
       if num == sum:  
            print(num)  


# # 19. pyhton code for method overloading

# In[53]:


class Area:
    def find_area(self,a=None,b=None):
        if a!=None and b!=None:
            print("Area of Rectangle:",(a*b))
        elif a!=None:
            print("Area of square:",(a*a))
        else:
            print("Nothing to find")
obj1=Area()
obj1.find_area()
obj1.find_area(10)
obj1.find_area(10,20)


# In[54]:


# First product method.
# Takes two argument and print their
# product
def product(a, b):
    p = a * b
    print(p)

# Second product method
# Takes three argument and print their
# product
def product(a, b, c):
    p = a * b*c
    print(p)

# Uncommenting the below line shows an error	
# product(4, 5)

# This line will call the second product method
product(4, 5, 5)


# In[ ]:




