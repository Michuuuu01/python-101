#Take two lists, say for example these two:
import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

#Extras:

#1 Randomly generate two lists to test this
#2 Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

#changing into set to take care about duplicates
a=set(a)
b=set(b)
## My function
def spajacz(k,l):
    c=[]
    for ele in k:
        for smt in l:
            if ele == smt:
                c.append(ele)
    return(set(c))

### for examples lists
numero_1=spajacz(a,b)
print(numero_1)

#1(Creating a new list)
d=[]
e=[]
#1(maing them random size)
y=random.randint(5,15)
z=random.randint(5,10)
#1(filling them with random numbers)
for element in range(1,y+1):
    d.append(random.randint(1,20))
for xdd in range(1,z+1):
    e.append(random.randint(1,20))
### for random lists
numero_2=spajacz(d,e)
print (numero_2)

