i=0
numbers=[]

while(i<3):
    num=int(input("Enter the no. "))
    numbers.append(num)
    i+=1

print(numbers)
total_sum=sum(numbers)

if total_sum>50:
    print("Lucky")
else:
    print("Not Lucky")