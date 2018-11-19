import xml.etree.ElementTree as ET


xml_data = """
<foo>
  <w l="el">one</w>
  <w l="le">two</w>
  <s t="ss">-</s>
  <w l="ll">three</w>
  <c>Z<sub>sss</sub>X<sub>ttt</sub>Y</c>
</foo>
"""

root = ET.fromstring(xml_data) # get root

print(root.tag)# foo

print("Immediate children:")

for immediate_child in root:
  print("  ", immediate_child.tag)
  print("    ", immediate_child.text)

  if immediate_child.tag == 'w':
     print("     l: ", immediate_child.attrib['l'])

  if immediate_child.tag == 'c':
#    ET.dump(immediate_child)

     for i in immediate_child.iter():
         print("       i: ", i)

     for s in immediate_child:
         print("       ", s.text)

     print("    ", s.tail) # Y
