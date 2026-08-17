""" 
Less than 10 --> Child
In between 10 & 18 --> Teenager
18> --> Adult 
"""

age=int(input("Enter your age "))

if age<=10:
    print("Child")
elif age>10 and age<=18:
    print("Teenager")
else:
    print("Adult")