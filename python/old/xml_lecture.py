# XML Processing
# Objective
# What is XML in Python XML Processing?
# XML Parser Architecture and API
# SAX (Simple API for XML)
# DOM (Document Object Model API)
# XML file
# Parsing XML with DOM
# Parsing XML with SAX
# make_parser()
# parse()
# parseString()
# Conclusion


### # XML Processing

"""
<root>  ##Parent or root

<child name="tanmay">  ## Child level or Element
<subchild>
</subchild>
</child>


<child name="tanmay">  ## Child level or Element
<subchild>
</subchild>
</child>

<child name="tanmay">  ## Child level or Element
<subchild>
</subchild>
</child>

</root>
"""

## What is difference between elements and attribute?

# Element
#<child>Apple</child>

# Element with attribute
#<child name="apple"></child>
#

# XMl =>

# Definition:

# In computing, Extensible Markup Language is a markup language that
# defines a set of rules for encoding documents in a format that is both
#  human-readable and machine-readable.
# The W3C's XML 1.0 Specification
#  and several other related specifications—all of them free open
# standards—define XML.

#
# What is XML used for?
#
# XML (Extensible Markup Language) Extensible Markup Language (XML) is
# used to describe data. The XML standard is a flexible way to create
# information formats and electronically share structured data via the
# public Internet, as well as via corporate networks
#
# What is the purpose of XML?
# XML (or markup languages derived from it) is used quite a lot in data
# transfer because it's an intermediate, platform independent format.
#  XML Schema can be used to enforce a particular structure and form in an
# XML document, and thus can be used to create custom markup languages
#
#
#
# What is difference between HTMLand XML?
#
# HTML is an abbreviation for HyperText Markup Language.
#  HTML was designed to display data with focus on how data looks.
# XML was designed to be a software and hardware independent tool
#  used to transport and store data, with focus on what data is. ...
#  XML is neither a programming language nor a presentation language.
#
#
# What is difference between JSON and XML?
#
# The fundamental difference between XML and JSON is that XML is a meta-language and JSON is a markup language. ... By contrast, JSON syntax has specific semantics built in: stuff between {} is an object, stuff between [] is an array, etc. A JSON parser, therefore, knows exactly what every JSON document means
#
#
# XML Features
# Excellent for handling data with a complex structure or atypical data.
# Data described using markup language.
# Text data description.
# Human- and computer-friendly format.
# Handles data in a tree structure having one-and only one-root element.
# Excellent for long-term data storage and data reusability.
#
# https://www.w3schools.com/xml/xml_whatis.asp
# XML


import xml.etree.ElementTree as ET
root = ET.parse("new.xml")
#print(root)

s='''<data year='2000'>
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
#root1=ET.fromstring(s)
#print(root1)

# find the root name
data=root.getroot()
#print(data.tag)
#print(data.attrib)


# FInding the Elements
# Elem=root.findall('country')
# print(Elem)
# for row in Elem:
#     print(row.find('rank').text)
#     print(row.find('year').text)
#     print(row.find('gdppc').text)
#     print(row.find('neighbor').attrib['name'])
    #print(row.tag)
    #print(row.attrib)

# update

#Elem=root.findall('country')
# print(Elem)
# for row in Elem:
#     rank=int(row.find('rank').text)+100
#     row.find('rank').text=str(rank)
#
# dumpval = ET.dump(root)
# root.write("new.xml")

# delete

# Elem=root.findall('country')
# # print(Elem)
# for row in Elem:
#     rank=int(row.find('rank').text)
#     if rank > 100:
#         row.remove(row.find('rank'))
#
# dumpval = ET.dump(root)
# root.write("new1.xml")


# create

# < student>
#<name> Tanmay
#</name>
#</student>


student=ET.Element("Student")
name=ET.SubElement(student,"name",{"name":"tanmay"})
value=ET.SubElement(name,"Age").text="Example"
print(ET.dump(student))
root.write("root1.xml")









