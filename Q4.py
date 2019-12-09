#Given the following two sets find the intersection and remove those elements from the
#first set.
#Given:
#>> First Set {65, 42, 78, 83, 23, 57, 29}
#>> Second Set {67, 73, 43, 48, 83, 57, 29}
#Expected Outcome:
#>> Intersection is {57, 83, 29}
#>> First Set after removing common element {65, 42, 78, 23}


set1  = {23, 42, 65, 57, 78, 83, 29}
set2 = {57, 83, 29, 67, 73, 43, 48}

a = set1.intersection(set2)
print("Intersection is ", a)
for i in a:
  set1.remove(i)

print(f"First Set after removing common element {set1}")
