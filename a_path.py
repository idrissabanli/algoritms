import random
# a = [[gedilecek_yol, oldugu_yerden_mesafe, cemi, yerlesme]]
a = [[0,0,0,1], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

a = []
array_count = 10

f_i, f_j = random.randint(0, array_count-1), random.randint(0, array_count-1)
l_i, l_j = random.randint(0, array_count-1), random.randint(0, array_count-1)

print(f_i, f_j)
print(l_i, l_j)
c_i, c_j = f_i, f_j




for i in range(array_count):
    a.append([])
    for j in range(array_count):
        if i == 0 and j ==0:
            a[i].append([0,0,0,1])
        else:
            a[i].append([0,0,0,0])

while (c_i, c_j) != (l_i, l_j):
    min_element = 1000
    min_element_ci = 0
    min_element_cj = 0
    if c_j < len(a[c_i])-1 and a[c_i][c_j+1][2] == 0:
        a[c_i][c_j+1][0] = 10*(abs(l_i-c_i) + abs(l_j-(c_j+1)))
        a[c_i][c_j+1][1] += 10
        a[c_i][c_j+1][2] = a[c_i][c_j+1][0] + a[c_i][c_j+1][1]
        if min_element > a[c_i][c_j+1][2]:
            min_element = a[c_i][c_j+1][2]
            min_element_ci = c_i
            min_element_cj = c_j+1
    if c_j > 0 and a[c_i][c_j-1][2] == 0:
        a[c_i][c_j-1][0] = 10*(abs(l_i-c_i) + abs(l_j-(c_j-1)))
        a[c_i][c_j-1][1] += 10
        a[c_i][c_j-1][2] = a[c_i][c_j-1][1] + a[c_i][c_j-1][0]
        if min_element > a[c_i][c_j-1][2]:
            min_element = a[c_i][c_j-1][2]
            min_element_ci = c_i
            min_element_cj = c_j-1
    if c_i > 0 and a[c_i-1][c_j][2] == 0:
        a[c_i-1][c_j][0] = 10*(abs(l_i-(c_i-1)) + abs(l_j-c_j))
        a[c_i-1][c_j][1] += 10
        a[c_i-1][c_j][2] = a[c_i-1][c_j][1] + a[c_i-1][c_j][0]
        if min_element > a[c_i-1][c_j][2]:
            min_element = a[c_i-1][c_j][2]
            min_element_ci = c_i-1
            min_element_cj = c_j
    if c_i < len(a)-1 and a[c_i+1][c_j][2] == 0:
        a[c_i+1][c_j][0] = 10*(abs(l_i-(c_i+1)) + abs(l_j-c_j))
        a[c_i+1][c_j][1] += 10
        a[c_i+1][c_j][2] = a[c_i+1][c_j][1] + a[c_i+1][c_j][0]
        if min_element > a[c_i+1][c_j][2]:
            min_element = a[c_i+1][c_j][2]
            min_element_ci = c_i+1
            min_element_cj = c_j
    if c_i < len(a)-1 and c_j< len(a[c_i])-1 and a[c_i+1][c_j+1][2] == 0:
        a[c_i+1][c_j+1][0] = 10*(abs(l_i-(c_i+1)) + abs(l_j-(c_j+1)))
        a[c_i+1][c_j+1][1] += 14
        a[c_i+1][c_j+1][2] = a[c_i+1][c_j+1][1] + a[c_i+1][c_j+1][0]
        if min_element > a[c_i+1][c_j+1][2]:
            min_element = a[c_i+1][c_j+1][2]
            min_element_ci = c_i+1
            min_element_cj = c_j+1
    if c_i > 0  and c_j > 0 and a[c_i-1][c_j-1][2] == 0:
        a[c_i-1][c_j-1][0] = 10*(abs(l_i-(c_i-1)) + abs(l_j-(c_j-1)))
        a[c_i-1][c_j-1][1] += 14
        a[c_i-1][c_j-1][2] = a[c_i-1][c_j-1][1] +a[c_i-1][c_j-1][0]
        if min_element > a[c_i-1][c_j-1][2]:
            min_element = a[c_i-1][c_j-1][2]
            min_element_ci = c_i-1
            min_element_cj = c_j-1
    if c_i > 0 and c_j < len(a[c_i])-1 and a[c_i-1][c_j+1][2] == 0:
        a[c_i-1][c_j+1][0] = 10*(abs(l_i-(c_i-1)) + abs(l_j-c_j+1))
        a[c_i-1][c_j+1][1] += 14
        a[c_i-1][c_j+1][2] = a[c_i-1][c_j+1][1] + a[c_i-1][c_j+1][0]
        if min_element > a[c_i-1][c_j+1][2]:
            min_element = a[c_i-1][c_j+1][2]
            min_element_ci = c_i-1
            min_element_cj = c_j+1
    if c_j > 0 and c_i < len(a[c_i])-1 and a[c_i+1][c_j-1][2] == 0:
        a[c_i+1][c_j-1][0] = 10*(abs(l_i-(c_i+1)) + abs(l_j-(c_j-1))) 
        a[c_i+1][c_j-1][1] += 14
        a[c_i+1][c_j-1][2] = a[c_i+1][c_j-1][1] + a[c_i+1][c_j-1][0]
        if min_element > a[c_i+1][c_j-1][2]:
            min_element = a[c_i+1][c_j-1][2]
            min_element_ci = c_i+1
            min_element_cj = c_j-1

    print(min_element, min_element_ci, min_element_cj)
    c_i = min_element_ci
    c_j = min_element_cj
    # for i, el in enumerate (a):
    #     print()
    #     # print(i)
    #     for j in el:
    #         print(j, end=',')
    # input()

