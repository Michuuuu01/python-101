# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

num=int(input("plis give me a number ;) "))


#list of divisiors
lst=[]

#range of our posible divisiors
x = range(1,num+1)


for elemnt in x:
    if num % elemnt == 0:
        lst.append(elemnt)
print(lst)
 