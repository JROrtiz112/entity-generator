from string import Template

def fileGenerator(classItem):
    classFile = open('templates/class.txt')
    attributeFile = open('templates/attribute.txt')

    attribute = attributeFile.read()
    class_t = classFile.read()

    classTemplate = Template(class_t)
    attributeTemplate = Template(attribute)

    attributes = ''

    for item in classItem.getData():
        attributes += attributeTemplate.substitute(item) + "\n"

    class_dict = dict(name=classItem.name, attributes = attributes[:-2])
    file = classTemplate.substitute(class_dict)

    classFile.close()
    attributeFile.close()

    return (file, classItem.name)