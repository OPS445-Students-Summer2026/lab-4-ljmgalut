t1 = ('Prime', 'Ix', 'Secundus', 'Caladan')
t2 = (1, 2, 3, 4, 5, 6)

print(t1[0])
print(t2[2:4])

print('Ix' in t1)
print('Geidi' in t1)

# This will FAIL (intentionally shown in lab explanation)
# t2[1] = 10

t3 = t2[2:3]
print(t3)

for item in t1:
    print('item: ' + item)
