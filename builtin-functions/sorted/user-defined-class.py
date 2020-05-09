class CLS:

      def __init__(self, val):

          self.val = val

      def __lt__(self, other):
          return self.val < other.val

      def __repr__(self):
          return 'CLS(' + str(self.val) + ')'


L = [ CLS(10),  CLS( 4), CLS(22), CLS( 8) ]

print(sorted(L))
#
#  [CLS(4), CLS(8), CLS(10), CLS(22)]
