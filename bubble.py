a = [4,3,57,78,23,46,75,56,2,35,22,-4,25,546,-4]

for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)