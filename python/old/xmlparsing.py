
# Import Libary
from xml.etree import ElementTree

# XML
# XML Advantage
# Difference between xml and html
# XML NameSpaces
# Root
# Root Attrib and Tags
# Element
# SubElement
# Element Tags and arrtubutes
# Modify Json Data
# Delete Elements
# Create New Json File using ElementTree
# SAX (Simple API for XML)
# DOM (Document Object Model API)
# Parsing XML with DOM
# Parsing XML with SAX



# XML :
    #1 XML stands for Extensible Markup Language
    #2. create a document of hierarchical structure.
    #3. A markup language uses a set of additional items called markups
    #4. xml contains content (i.e. text, images etc.)
    #5. XML is recommended by W3C.

# XML Rule
    #Element names are case-sensitive
    #Element names must start with a letter or underscore
    #Element names cannot start with the letters xml (or XML, or Xml, etc)
    #Element names can contain letters, digits, hyphens, underscores, and periods
    #Element names cannot contain spaces

#Example of XML Document

'''<?xml version="1.0" ?>
<root>
<design>html</design>
<programming>php</programming>
</root>'''


# Advantages of xml
    # 1.  xml supports UNICODE
    # 2.  all most all the human readable written languages can be communicated using xml.
    # 3. XML is used both on and offline for storing and processing data.
    # 4. XML follows international standards.
    # 5.Being platform independent, it has lots benefits.

# Disadvantage
    # 1. XML needs an application processing system . There are no browsers yet which can read XML.



#  Difference between xml and html

    # Html tags are predefined, whereas xml tags are not.
    # Html is used to display data, taking care of how data is being presented. xml is used to carry data. It takes care of how data works.
    # Opening and closing tags of an xml document must be of same case. html does not have any such restriction.
    # In xml, end tags are required for well-formed (i.e. valid) document. But not in html.
    # Quotes are required around attributes values in xml, in html it is not required.
    # Slash (/) required in empty tags as far as xml is concerned, html does not need that.


# why using XML?
    # XML can be integrated to all the feasible data format like form text and numbers to multimedia like sound, image etc
    # No programming required to modify the presentation of data
    # Open and extensible
    # XML is the endorsed industry standard of the World Wide Web Consortium (W3C) and is supported by all leading software providers.

#  Root

#XML File
'''<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
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

tree=ElementTree.parse('new.xml')
root=tree.getroot()
# Find Tagd
tags= root.tag
print(tags)
# Find attrib
#root.attrib

# Find all Child

for child in root:
    print(child.tag, child.attrib)

for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)

# Modify XML

for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'yes')

tree.write('output.xml')

# Ddelete XML

for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write('output.xml')


# Create XML
a = ElementTree.Element('a')
b = ElementTree.SubElement(a, 'b')
c = ElementTree.SubElement(a, 'c')
d = ElementTree.SubElement(c, 'd')
print(ElementTree.dump(a))

# NameSpace
    #namespace declaration is xmlns: prefix="URI".
    # Solving the Name Conflict Using a Prefix
    # The namespace URI is not used by the parser to look up information.
    # The purpose of using an URI is to give the namespace a unique name.


# NameSpace Example
'''<table xmlns="http://www.example.org/TR/html4/">
  <tr>
    <td>Apples</td>
    <td>Bananas</td>
  </tr>
</table>'''

# Use of Namespace
 # XSLT is a language that can be used to transform XML documents into other formats.
 # XSLT (eXtensible Stylesheet Language Transformations) is the recommended style sheet language for XML.
#XSLT you can transform an XML document into HTML.

 # DOM

    #https://www.w3schools.com/xml/nodetree.gif
    #The DOM defines a standard for accessing and manipulating documents:
    # The XML DOM defines a standard way for accessing and manipulating XML documents. It presents an XML document as a tree-structure.




# XML Elements
    #Elements are the basic building blocks of an XML document.

#Simple API for XML (SAX)
'''− Here, you register callbacks for events of interest and then let the parser proceed 
through the document. This is useful when your documents are large or you have memory 
limitations, it parses the file as it reads it from the disk and the entire file is never
stored in the memory.'''

#Document Object Model (DOM) API
'''− This is a World Wide Web Consortium recommendation wherein the entire file is read into
the memory and stored in a hierarchical (tree-based) form to represent all the features of
an XML document.'''

 #Note 1- SAX obviously cannot process information as fast as DOM

