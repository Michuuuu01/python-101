#Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

#xtras:

#1 Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#2 Write this in one line of Python.
#3 Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
b=[]

def mniejsze(a):
    for num in a:
        if num <5:
            b.append(num)
        else:
            pass
mniejsze(a)
print(b)

#2 
print( [ x for x in a if x<5 ] )

#3
c=[]
per_inp=input("Gie a number ;) ")
for num in a:
    if num<int(per_inp):
        c.append(num)
    else:
        pass
print(c)
