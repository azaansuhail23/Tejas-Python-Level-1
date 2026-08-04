set1=set()
set2=set()

set1.add(1)
set1.add(2)
set1.add(3)
set1.add(4)
set1.add(5)

set2.add(3)
set2.add(5)
set2.add(7)
set2.add(8)

union=set1.union(set2)
print("Union : ",union)

intersection=set1.intersection(set2)
print("Intersection : ",intersection)

set_difference=set1.difference(set2)
print("Set Difference : ",set_difference)