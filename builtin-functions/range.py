print(type(range(5))) # <class 'range'>

print(range(   7))    # range(0, 7)
print(range(3, 7))    # range(3, 7)

for i in range(4):
    print(i)
    # 0
    # 1
    # 2
    # 3

for i in range(5, 8):
    print(i)
    # 5
    # 6
    # 7

for i in range(-2, 2):
    print("  " + str(i))
    # -2
    # -1
    # 0
    # 1

for i in range(342, 600, 100):
    print(i)
    # 342
    # 442
    # 542

# print('-'.join(range(7)))

#  TypeError: range() integer step argument expected, got float.
#  print(range(5, 7, 0.333))

print([ x * 0.333 for x in range(5 * 3, 7 * 3) ])  # [4.995, 5.328, 5.6610000000000005, 5.994000000000001, 6.327, 6.66]