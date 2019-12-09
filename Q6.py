#Remove duplicate from a list and create a tuple and find the min and max number.
#Given:
#sampleList = [87, 45, 41, 65, 94, 41, 99, 94]
#Expected Outcome:
#>> unique items [87, 45, 41, 65, 99]
#tuple (87, 45, 41, 65, 99)
#min: 41
#max: 99


sampleList = [87, 45, 41, 65, 94, 41, 99, 94]

uniqueitems = list(dict.fromkeys(sampleList))
print(f"Unique items {uniqueitems}")

tuple = tuple(uniqueitems)
print(tuple)
print(f"Min : {min(tuple)}")
print(f"Max : {max(tuple)}")
