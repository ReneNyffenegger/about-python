dict_1 = {'x'  : 'eggs', 'y'    : 'why'  , 'num': 99}
dict_2 = {'num':  42   , 'hello': 'world'           }

dict_merged = {**dict_1, **dict_2}

for k, v in dict_merged.items():
    print(f"{k} = {v}")
