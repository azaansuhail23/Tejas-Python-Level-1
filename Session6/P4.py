tup1=("Azaan",12,13,True,"Tejas",12,13,2,2,12, "Tejas",False)
print(tup1)

print(tup1.count(12)) # 3
print(
    tup1.index("Tejas")
)  # Searches the tuple for a specified value and returns the position/index of where it was found


index=len(tup1)-1

while(index>=0):
    if tup1[index]=="Tejas":
        print(index)
    
    index=index-1