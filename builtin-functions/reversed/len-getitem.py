class seq_one_to_four:

      def __len__(self):
          return 4

      def __getitem__(self, i):
          if i == 0: return 'one'
          if i == 1: return 'two'
          if i == 2: return 'three'
          if i == 3: return 'four'


seq = seq_one_to_four()

for e in reversed(seq):
    print(e)
