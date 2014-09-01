from   bs4 import BeautifulSoup

soup = BeautifulSoup(
  """<foo><c>text one<sub>ttt</sub>text two<sub>uuu</sub>text three</c></foo>"""
)


def descend(node, level):
    for child in node.contents:

        if child.name != None:
           print "  " * level, "<" + child.name+ ">"
           descend(child, level+1)
           print "  " * level, "</"+ child.name+ ">"
        else:
           print "  " * level, " " + child.string

descend(soup, 0)
