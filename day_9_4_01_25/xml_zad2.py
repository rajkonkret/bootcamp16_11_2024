import xml.etree.ElementTree as ET


def GenerateXML(filename):
    root = ET.Element("Catalog")

    m1 = ET.Element('mobile')
    root.append(m1)

    b1 = ET.SubElement(m1, "brand")
    b1.text = "Redmi"

    b2 = ET.SubElement(m1, 'price')
    b2.text = "6999"

    m2 = ET.Element('mobile')
    root.append(m2)

    c1 = ET.SubElement(m2, "brand")
    c1.text = "Samsung"

    c2 = ET.SubElement(m2, "price")
    c2.text = "9999"

    m3 = ET.Element("mobile")
    root.append(m3)

    d1 = ET.SubElement(m3, "brand")
    d1.text = "Apple"

    d2 = ET.SubElement(m3, "price")
    d2.text = "7999"

    tree = ET.ElementTree(root)

    with open(filename, "wb") as file:
        tree.write(file, xml_declaration=True)


# xml_declaration=True dodaje nagłowek xml
if __name__ == '__main__':
    GenerateXML("catalog.xml")

# <?xml version='1.0' encoding='us-ascii'?>
# <Catalog>
#     <mobile>
#         <brand>Redmi</brand>
#         <price>6999</price>
#     </mobile>
#     <mobile>
#         <brand>Samsung</brand>
#         <price>9999</price>
#     </mobile>
#     <mobile>
#         <brand>Apple</brand>
#         <price>7999</price>
#     </mobile>
# </Catalog>
