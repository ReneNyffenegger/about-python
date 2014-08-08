from xml.dom import minidom

xml_data = """
<foo>
    <bars>
        <bar id="bar 01">one  </bar>
        <bar id="bar 02">two  </bar>
        <bar id="bar 02">three</bar>
    </bars>
    <baz>bbbaazzz</baz>
</foo>
"""

#  Alternatively, to parse a file, use minidom.parse(file_name)
xmldoc = minidom.parseString(xml_data)


for bar in xmldoc.getElementsByTagName('bar'):
    print "id " + bar.attributes['id'].value + " = " + bar.childNodes[0].nodeValue
