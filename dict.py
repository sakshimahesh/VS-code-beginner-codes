band = { 
        "vocals": "plant",
        "guitar": "strings"}
band2 = dict(vocals="plant", guitar="strings")
print(band)
print(band2)

print(band2.get("guitar"))

print(band2.keys())
print(band2.values())
print(band2.items())

#print("guitar" in band2)
#print(band2.pop("plant"))
#rint(band2)

# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1


value=0
while value <=10:
    value +=1
    if value == 5:
        continue
    print(value)
else:
    print("")
    
names = ["bcg", "kpmg"]
for x in names:
    if x=="kpmg":
        break
    print(x)

for x in range(4):
    print(x)
    

    
    
    
