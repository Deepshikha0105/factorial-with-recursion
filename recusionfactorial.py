def fact(n):
    if n<= 1:
        return 1
    else:
        a= n* fact(n-1)
        return a

s= int(input("enter a number: "))
q= fact(s)
print(f"the factorial of {s} is " + str(q))
