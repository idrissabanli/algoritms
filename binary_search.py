a = [75,56,2,35,22,-4,25,546,4,3,-7,78,23,46,]
find = 35

for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)
founded = False
lena = 0
lenb= len(a)
while not founded:    
    middle_element = a[(lenb + lena)//2]
    print(middle_element)
    if find == middle_element:
        founded = (lenb + lena)//2
    elif find >= middle_element:
        lena = (lenb + lena)//2
    else:
        lenb = (lenb + lena)//2
    print(founded, lena, lenb)
    input()

print(founded)