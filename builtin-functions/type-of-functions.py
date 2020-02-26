built_in_funcs = [                        
  abs          , all         , any        , ascii      , bin        ,
  bool         , breakpoint  , bytearray  , bytes      , callable   ,
  chr          , classmethod , compile    , complex    , delattr    ,
  dict         , dir         , divmod     , enumerate  , eval       ,
  exec         , filter      , float      , format     , frozenset  ,
  getattr      , globals     , hasattr    , hash       , help       ,
  hex          , id          , input      , int        , isinstance ,
  issubclass   , iter        , len        , list       , locals     ,
  map          , max         , memoryview , min        , next       ,
  object       , oct         , open       , ord        , pow        ,
  print        , property    , range      , repr       , reversed   ,
  round        , set         , setattr    , slice      , sorted     ,
  staticmethod , str         , sum        , super      , tuple      ,
  type         , vars        , zip        , __import__
]


for f in built_in_funcs:
  #
  # Special check because help does not have the __name__ attribute:
  #
    name = f.__name__ if hasattr(f, '__name__') else 'help'

    print('{:15s} {:s}'.format(name, str(type(f))))
