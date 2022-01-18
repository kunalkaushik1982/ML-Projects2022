from ast import Str
from operator import truediv
import string
from xmlrpc.client import Boolean


print("Hello 2022", end='')
# firstname=input("Enter your first name :")
# print("Your Name is: ", firstname)
print("Kunal","Mrinal","Harsh","Aarya", sep='#')



# Python Support 3 categories of datatypes:
#     Basic Types - Integer, Float, Boolean,string, complex
#     Container Types - List, Set, Dictionary, Tuples
#     User Defined Type - Class
#Integer
print(4)
print(5000000000000000000000000000000000000000000000000000000000000000000000000000000)
print(1e309)

#Float
print(4.5)
print(1.7e307)
print(1.7e308)
print(1.7e309)

#Boolean
print(True)
print(False)

#Complex
print(4+5j)
print(4+9j)

#String
print('Kunal')
print("Kunal")
print("""Kunal""")

#List
print([1,2,3,4,5])

#Tuples
print((1,2,3,4,5))

#Set
print({1,2,3,4,5})

#Dictionary
print({"Name":"Kunal","Age":30,"Gender":"Male"})

#//////////////////////////////////
#Variable
#Dynamic Typing & Dynamic Binding
name=4
print(name)
name='kuanl'
print(name)
name=True
print(name)

#Special Syntax
a=4;b=5;c=6
print(a)
print(b)
print(c)

a,b,c=4,5,6
print(a)
print(b)
print(c)

a=b=c=6
print(a)
print(b)
print(c)

#///////////////
#Keyword
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
#/////////////////////////
#Type Conversion
print(int(2))
print(float(2))
print(bool(1))
print(complex(9))
print(list("Hello"))

