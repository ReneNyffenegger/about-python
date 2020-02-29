import ctypes

result = ctypes.windll.user32.MessageBoxW(
   0            ,
  'Yes or no?'  ,
  'Choose wisly',
    4           |  # MB_YESNO
   32              # MB_ICONQUESTION
)

if   result == 6:            # ID_YES
     print('Good for you!')
else:
     print('Well, do you want to talk about it?')
