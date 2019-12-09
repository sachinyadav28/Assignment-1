sampleList = [87, 45, 41, 65, 94, 41, 99, 94]

uniqueitems = list(dict.fromkeys(sampleList))
print(f"Unique items {uniqueitems}")

tuple = tuple(uniqueitems)
print(tuple)
print(f"Min : {min(tuple)}")
print(f"Max : {max(tuple)}")
