#  Returns an array of the modal (most common) value in the passed array.

import scipy.stats

print scipy.stats.mode( [  4, 5, 4, 6, 4, 2, 4, 4, 4 ])  # 4 is most common, it appears six times
# (array([ 4.]), array([ 6.]))



