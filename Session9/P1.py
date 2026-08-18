# 5!=1*2*3*4*5

num=int(input("Enter the num "))

res=1  #ans -> Factorial 
i=1

while(i<=num):
    res = res*i
    i=i+1

print(f"Factorial of {num} is =",res)