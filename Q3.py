z=input("Type letters and digits!! ")
l=0
d=0
for y in z:
    if y.isdigit():
        d = d + 1
    else:
        l=l + 1

print(f"LETTERS  {l}")
print(f"DIGITS  {d}") 
