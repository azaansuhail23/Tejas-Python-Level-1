name = input("Enter the name plaese ")

Physics = int(input("Enter the Physics Marks "))
Chemistry = int(input("Enter the Chemistry Marks "))
Mathematics = int(input("Enter the Mathematics Marks "))

total_marks = Physics + Chemistry + Mathematics
average_marks = total_marks // 3

print("Total Marks = ", total_marks)
print("Average Marks = ", average_marks)

# 50 percent criteria for pass and fail

if total_marks > 150:
    print(f"Congratulations {name} is Passed !")
else:
    print(f"Sorry {name} is Failed !")
