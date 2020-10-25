import sys

path_to_script = sys.argv[0]
with open(path_to_script) as f:
     this_script_as_text  = f.read()

print(this_script_as_text)
