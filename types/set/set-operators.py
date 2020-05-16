even  = { 2, 4, 6, 8, 10, 12 }
odd   = { 1, 3, 5, 7,  9, 11 }
prime = { 2, 3, 5, 7, 11     }

print(prime - odd)
#
# {2}

print(prime & even)
#
# {2}

print(even | prime)
#
# {2, 3, 4, 5, 6, 7, 8, 10, 11, 12}

print(odd ^ prime)
#
# {1, 2, 9}
