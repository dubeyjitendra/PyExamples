# XML
# XML Advantage
# Difference between xml and html
# XML NameSpaces
# Root
# Root At
# SubElementtrib and Tags
# # Element
# Element Tags and arrtubutes
# Modify XML Data
# Delete Elements
# Create New XML File using ElementTree
# SAX (Simple API for XML)
# DOM (Document Object Model API)
# Parsing XML with DOM
# Parsing XML with SAX
# XML
#syntax
'''<?xml version="1.0" ?>
<root>
</root>'''
'''<?xml version="1.0"?>
<data>
    <country name="India">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>'''

from xml.etree import ElementTree

# Read
tree=ElementTree.parse("D:\Python_class\S_Lec1\student.xml")
root=tree.getroot()
#print(root)
#print(root.tag)
#print(root.attrib)
#tree1=ElementTree.parse("D:\Python_class\S_Lec1\student.xml")
#for row1 in tree1.findall('student'):
    #print(row1.tag,row1.attrib)

'''for row in root.iter('country'):
    print(row.tag,row.attrib)'''

'''for row in root.findall('student'):
    age=row.find('age').text
    address = row.find('address').text
    salary=row.find('salary').text
    #print(row.attrib['name'],age,address,salary)
    print("Name : {0} , Age : {1}, Address : {2} ,salary : {3} ".format(row.attrib['name'],age,address,salary))

    #print(row.tag,row.attrib)'''

# Modify single element
'''for root1 in root.iter('student'):
    if(root1.attrib["name"]=="Ajai"):
        for row in root.iter('age'):
            if(row.text=="60"):
                age=int(row.text)+1
                row.text=str(age)

dumpval=ElementTree.dump(tree)
print(ElementTree.dump(tree))'''
#tree.write('dumpval.xml')

# delete XML FIles
for root1 in root.iter('student'):
    if(root1.attrib["name"]=="Ajai"):
        for row in root.iter('age'):
            if(row.text=="60"):
                root.remove(root1)

dumpval=ElementTree.dump(tree)

'''root = ET.Element("root")
doc = ET.SubElement(root, "doc")

ET.SubElement(doc, "field1", name="blah").text = "some value1"
ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"
tree = ET.ElementTree(root)
print(ET.dump(tree))'''

# Create XML
'''root1=ElementTree.Element("root")
doc=ElementTree.SubElement(root1,"student1")
ElementTree.SubElement(doc,"S1",name="Ajai").text="12345"
ElementTree.SubElement(doc,"S2",name="Jomesh").text="12345"
tree1=ElementTree.ElementTree(root1)
print(ElementTree.dump(tree1))
tree1.write("D:\\root1.xml")'''













'''a = ElementTree.Element('a')
b = ElementTree.SubElement(a, 'b')
c = ElementTree.SubElement(a, 'c')
d = ElementTree.SubElement(c, 'd')
print(ElementTree.dump(a))'''

