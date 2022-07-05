from fileGenerator import *
import os
from classes.mainClass import Class

def main():
    # attributes = []
    # attributes.append(dict(default='{ default: 0 }', attribute='cost', type='number'))
    # attributes.append(dict(default='{ default: true }', attribute='isMale', type='boolean'))
    # attributes.append(dict(default='', attribute='name', type='string'))

    classFile = Class('Superstar')
    classFile.append(['{ default: 0 }', 'cost', 'number'])
    classFile.append(['{ default: true }', 'isMale', 'boolean'])
    classFile.append(['', 'name', 'string'])

    attributes2 = []
    attributes2.append(dict(default='{ default: 0 }', attribute='cost', type='number'))
    attributes2.append(dict(default='{ default: true }', attribute='isMale', type='boolean'))
    attributes2.append(dict(default='', attribute='name', type='string'))

    files = []
    file = fileGenerator(classFile)
    files.append(file)
    # file = fileGenerator(attributes2, 'Superstar2')
    # files.append(file)

    isPrint = input('Do you like to print the file(s)?: Y/n ')
    if isPrint.lower() == 'y':
        path = os.getcwd() + '/files'
        if not os.path.isdir(path):
            os.mkdir(path)
        for file in files:
            printFile = open(f'{path}/{file[1].lower()}.entity.ts', "w")
            printFile.write(file[0])
            printFile.close()

if __name__ == '__main__':
    main()