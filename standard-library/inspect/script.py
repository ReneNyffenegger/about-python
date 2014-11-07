import inspect

def xyz(ab, cd = 'foo bar', ef = 42):
    pass


a  = inspect.getargspec(xyz)

print "Arguments:"
for arg in a.args:
    print "  " + arg


print "\nDefaults:"
for def_ in a.defaults:
    print "  " + str(def_)


# Arguments:
#   ab
#   cd
#   ef
# 
# Defaults:
#   foo bar
#   42
