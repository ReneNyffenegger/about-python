#!/usr/bin/python3

pairs = [ (1, 'one'  ),
          (2, 'two'  ),
          (3, 'three')
        ]

nums, words = zip(*pairs)

print(nums )
# (1, 2, 3)

print(words)
# ('one', 'two', 'three')
