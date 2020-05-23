import os.path

for I in __file__, '.', 'xyz':

    print('File                {:31s}  {}'.format(os.path.basename(I), 'exists' if os.path.isfile(I)  else 'does not exist'))
    print('Directory           {:31s}  {}'.format(os.path.basename(I), 'exists' if os.path.isdir(I)   else 'does not exist'))
    print('Directory or file   {:31s}  {}'.format(os.path.basename(I), 'exists' if os.path.exists(I)  else 'does not exist'))
