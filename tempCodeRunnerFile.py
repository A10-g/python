31
x=input("enter your first name")
y=input("enter your last name")

print(y+" "+x)

#2
x=input("enter comma separated numbers:")
list = x.split(",")
tuple= tuple(list)
print('list:',list)
print('tuple:',tuple)

#3
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0])
print(color_list[3])







#6
from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)

#7
my_list=[1, 5, 8, 3]
print(3 in my_list)
print(-1 in my_list)


#10
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))

#17
import time

start = time.time()

for i in range(3):
    print("hello")

end = time.time()
print("the execution time is:" ,end-start)

#18
import os
print('Get current working directory : ', os.getcwd())

#20
x=int(input("enter first number"))
y=int(input("enter second number"))
z=int(input("enter second number"))

a1=min(x,y,z)
a3=max(x,y,z)
a2=(x+y+z)-a1-a3

print(a1,a2,a3)

#24
import sys
a=sys.getsizeof(12)
print(a)

#Arrays 
#1
from array import *
array_num=array('i',[1,2,3,4,5])
print(array_num[0])
print(array_num[1])
print(array_num[2])

#dictionary
#2
my_dictionary ={0: 10, 1: 20}
print(my_dictionary)
my_dictionary.update({3:30})
print(my_dictionary)

#3
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic2.update(dic3)

dic1.update(dic2)
print(dic1)

#4

my_dictionary={1:10,2:20,3:30}

for i in my_dictionary.items():
    print(i)

#5

x=int(input("enter number x:"))
y={}

for d in range(x+1):
    
    if d==0:
        continue
    z={d:d*d}
    y.update(z)

print(y)

#6

my_dictionary={1:1,2:2,3:3,4:4}

my_dictionary.remove(1)



















































































































































































































































































































































