with open('iter.txt') as txt_file:
     for txt_line in txt_file:
      #
      #  use end='' to omit printing new-lines
      # (The newline is already present in txt_line)
      #
         print (txt_line, end='')
