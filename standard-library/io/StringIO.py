import io

txt = 'Hello world!'

txt_io = io.StringIO(txt)

print(txt_io.getvalue())

txt_io.seek(6)
txt_io.write('there')

print(txt_io.getvalue())
