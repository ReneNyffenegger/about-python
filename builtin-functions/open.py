#
#    Links:
#      ../misc/stdout_or_file.py
#
f_in = open(__file__, 'r')

print("".join( f_in.readlines() ))

f_out = open('open.out', 'w')
f_out.write("Hello world\n")
f_out.write("The number is: 42\n")
f_out.close()
