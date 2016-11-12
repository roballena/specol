from os import path
from watson_developer_cloud import NaturalLanguageClassifierV1
from construct_cpp import generateIOHeader, generateMainMethod
from cpp_command_factory import get
from compiler import compileBinary
from time import sleep
import sys

natural_language_classifier = NaturalLanguageClassifierV1(
  username='0d8af576-53ef-4feb-9511-7cb30a2b1728',
  password='UbCAJZSXHbkA')

def readSpec(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def getFullCommand(statement):
    command = natural_language_classifier.classify('e3ca6dx107-nlc-5855', statement)["top_class"]
    args = natural_language_classifier.classify('f48968x109-nlc-4949', statement)["top_class"]
    return (command,args)

def generateCPPCode(codes):
#     chooseLanguage()
    print 'Generating CPP code'
    lineOfCodes = ''
    for code in codes:
        lineOfCodes = lineOfCodes + get(getFullCommand(code))
    file_output = generateIOHeader() + generateMainMethod(lineOfCodes)
    
    return file_output

def chooseLanguage():
    sys.stdout.write("Choosing the best language for selected specification...")
    for i in range(1, 50):
        sleep(.2)
        sys.stdout.write('.')
    sys.stdout.write('DONE\n')
    print "Cpp 14 Chosen\n"
    
def createFile(fileName, content):
    # Open a file
    fo = open(fileName, "wb")
    fo.write(content);
    fo.close()
    print 'Code generation done!\n'

def getSpecLocation():
    file_path = path.relpath("sample.doc")
    return file_path

createFile("main.cpp", generateCPPCode(readSpec(getSpecLocation())))
compileBinary()