#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

a= input("write smth and i will write it in backwards :) ")
num=int((len(a)))
print(a[num:0:-1]+a[0])