def createMultiplier(t):

    def multiplyBy_t(v):
        return t*v

    return multiplyBy_t


mult_by_4 = createMultiplier(4)
mult_by_9 = createMultiplier(9)

print(mult_by_4(5)) # 20
print(mult_by_9(3)) # 27
