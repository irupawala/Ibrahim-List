
l = [00, 10, 20]
x1 = 2**3

for x in range(x1): 
    usedIndex = [l[i] for i in range(3) if ((x / 2 ** i) % 2) // 1 == 1]
#    usedIndex = [i for i in range(l)]
    print(usedIndex)
    
    

l = 3
x1 = 2**3

for x in range(x1):
    print(f"======================================= x = {x}")
    for i in range(l):
        print(f"i={i}")
        print(f"2**i = {2**i}")
        print(f"(x/2**i) = {(x/2**i)}")
        print(f"check={(x/2**i) % 2}")
        if (((x / 2 ** i) % 2) // 1 ) == 1 :
            print(f"=========yes======== i = {i}")