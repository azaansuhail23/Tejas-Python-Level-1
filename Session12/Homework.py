para=input("Enter your Paragraph : ")

split=para.split(' ')  #split contains a list of words of string  #NOTE : Split method of string needs a parameter you want to split.

print("Length : ", len(split))

if len(split)>=250:
    print("Passed")
else:
    print("Failed")




sentence='I, am, good'
split_comma=sentence.split(',')
print(len(split_comma))
print(split_comma)