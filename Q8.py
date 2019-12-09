rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict = {'A':47, 'B':69, 'C':76, 'D':97}
list1 = []

for items in rollNumber:
    if items in sampleDict.values():
        list1.append(items)

for items in rollNumber:
    if items not in sampleDict.values():
        rollNumber.remove(items)
        
print(f"New List {rollNumber}")
