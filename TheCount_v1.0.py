print(" __________________________")
print("|                          |")
print("|  Application: The Count  |")
print("|  Version: 1.0            |")
print("|__________________________|")

print()

Count = int(input("Count >>> "))
Count_UpTo = int(input("Count (up to) >>> "))

print()

for i in range(Count, Count_UpTo + 1):
    print(i)

print()