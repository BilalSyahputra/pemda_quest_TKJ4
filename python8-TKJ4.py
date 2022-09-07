list_integer = [1, 2, 3, 10, 100, 250]
list_string = ["RIVAI", "FAISAL", "UNTUNG", "ANJAS",]
list_mix = [20, "Arya", True, "Anjas"]

print("Data String:", list_string)
list_string[0] = "Dimas"
list_string[1] = "Jamil"
list_string[2] = "Ridho"
list_string[3] = "Naufal"
print ("Data setelan diubah:", list_string)

print("Data Mix:", list_mix)
list_mix[0] = 10
list_mix[1] = "Bilal"
list_mix[2] = False
list_mix[3] = "Ayu"
print ("Data setelan diubah:", list_mix)

# perulangan For

x = ["Naufal", "Fadli", "Abyan", "Desta"]
for y in x:
    print(y)

print("\n")
for i in  list_string:
    print(i)

x = [20, "Arya", True, "Anjas"]   
for y in x:
    print(y)

print("\n")
for i in  list_mix:
    print(i)

x = [1, 2, 3, 10, 100, 250]
for y in x:
    print(y)

print("\n")
for i in  list_integer:
    print(i)


