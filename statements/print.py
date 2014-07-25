#!/usr/bin/python

print "%f"    % 3.141             # 3.141000
print "%6.2f" % 3.141             #   3.14
print "%06.2f" % 3.141            # 003.14  

ar=[1, 2, 3]
tu=(7, 8, 9)

print ar                          # [1, 2, 3]
print tu                          # (7, 8, 9)

print "%d %d %d"    %  tu         # 7 8 9

print "{} {}".format(tu, 5)       # (7, 8, 9) 5


# print "%d %d %d" % ar  # TypeError: %d format: a number is required, not list
