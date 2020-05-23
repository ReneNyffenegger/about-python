words = 'one', 'TWO', 'three', 'four', 'Five'

for word in sorted(words):
    print(word)

print('')

for word in sorted(words, key = lambda w: w.upper()):
    print(word)
