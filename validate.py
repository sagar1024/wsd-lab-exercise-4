import xmlschema
xml_file = "WSDLabex4.xml"
xsd_file = "WSDLabex4.xsd"

validator = xmlschema.XMLSchema(xsd_file)
if validator.is_valid(xml_file):
    print("XML file is valid against the XSD schema.")
else:
    print("XML file is not valid against the XSD schema.")
    print(validator.validate(xml_file))