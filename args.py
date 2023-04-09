def add_num(name,*args):
    total=0 
    for num in args:
        total= total + num
    print(f"my name is {name}")
    return total
total=add_num(1,5,6,23,11,2,1)
print(total)