L1 = []

L1.append(2)
L1.append(3)

L2 = L1

L2.append(5)
L2.append(7)

for p in L1:
    print(p)

if (id(L1) != id(L2)):
    print('id differs')

if (L1 is L2):
    print('L1 is the same object as L2')
