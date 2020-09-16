from subprocess import Popen

proc = Popen(['gvim', __file__])
print('pid = {}'.format(proc.pid))
