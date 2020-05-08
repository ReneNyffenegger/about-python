#!/usr/bin/python3

class with_len:
    def __init__(self, cntTrue):
        self.cntTrue = cntTrue

    def __len__(self):

        print("__len__: cntTrue = " + str(self.cntTrue))

        self.cntTrue -= 1
        return self.cntTrue



L = with_len(4)


while L:
    print("Still in loop")

print("Loop exited")
