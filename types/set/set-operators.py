even = { 2, 4, 6, 8, 10, 12 }
odd  = { 1, 3, 5, 7,  9, 11 }
prim = { 2, 3, 5, 7, 11     }

print(prim - odd)
#
# {2}

print(prim & even)
#
# {2}

print(even | prim)
#
# {2, 3, 4, 5, 6, 7, 8, 10, 11, 12}

print(odd ^ prim)
#
# {1, 2, 9}
