x=int(input("Enter the first no. "))
y=int(input("Enter the second no. "))

oper=input("Enter + for addition , - for subtraction , * for multiplication, / for dividation operation ")

if oper=="+":
    print(x+y)
elif oper=='-':
    print(x-y)
elif oper=='/':
    if y==0:
        print("Invalid Operation will lead to undefined result !!")
    else:
        print(x/y)
elif oper=="*":
    print(x*y)
else:
    print("Invalid Operation")
