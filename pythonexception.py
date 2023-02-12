#Exception handling in python
#how to handle ZerodivisionError
a=10
b=0
c=0
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Denominator can't be 0")
finally:
    print("It will always execute irrespective of exception")
#finally: is used to close the resource(database,file,any external resource)

#How to handle IndexError in python
list1=[2,4,6,7,89,9]
try:
    a=list1[10]
    print(a)
except IndexError:
    print("Index out of range")

