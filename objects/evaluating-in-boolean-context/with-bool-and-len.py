#!/usr/bin/python3

class with_bool_an_len:
    def __init__(self, cntTrue):
        self.cntTrue = cntTrue

    def __bool__(self):

        print("__bool__: cntTrue = " + str(self.cntTrue))

        self.cntTrue -= 1
        return self.cntTrue >= 0

    def __len__(self):

        print("__len__: cntTrue = " + str(self.cntTrue))

        self.cntTrue -= 1
        return self.cntTrue >= 0 



L = with_bool_an_len(1)


print("Going to loop")
while L:
    print("Still in loop")

print("Loop exited")
#
#  Going to loop
#  __bool__: cntTrue = 1
#  Still in loop
#  __bool__: cntTrue = 0
#  Loop exited
