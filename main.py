from fileGenerator import *
import os
from classes.mainClass import Class

def main():
    files = []

    classFile = Class('Superstar')
    classFile.append(['{ default: 0 }', 'cost', 'number'])
    classFile.append(['{ default: true }', 'isMale', 'boolean'])
    classFile.append(['', 'name', 'string'])

    classFile2 = Class('Superstar2')
    classFile2.append(['{ default: 1 }', 'cost', 'number'])
    classFile2.append(['{ default: false }', 'isMale', 'boolean'])
    classFile2.append(['', 'name', 'string'])

    file = fileGenerator(classFile)
    files.append(file)
    file2 = fileGenerator(classFile2)
    files.append(file2)

    isPrint = input('Do you like to print the file(s)? Y/n: ')
    if isPrint.lower() == 'y':
        path = os.getcwd().removesuffix('entity-generator') + '/files'
        if not os.path.isdir(path):
            os.mkdir(path)
        for file in files:
            printFile = open(f'{path}/{file[1].lower()}.entity.ts', "w")
            printFile.write(file[0])
            printFile.close()

if __name__ == '__main__':
    main()