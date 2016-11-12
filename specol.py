from os import path
from watson_developer_cloud import NaturalLanguageClassifierV1
from construct_cpp import generateIOHeader, generateMainMethod
from cpp_command_factory import get
from compiler import compileBinary, runBinary

natural_language_classifier = NaturalLanguageClassifierV1(
  username='0d8af576-53ef-4feb-9511-7cb30a2b1728',
  password='UbCAJZSXHbkA')

def readSpec(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def getCommand(statement):
    classes = natural_language_classifier.classify('e82f62x108-nlc-5131', statement)
    return classes["top_class"].splitlines()
    
def generateCPPCode(codes):
    lineOfCodes = ''
    for code in codes:
        lineOfCodes = lineOfCodes + get(getCommand(code))
    file_output = generateIOHeader() + generateMainMethod(lineOfCodes)
    
    return file_output


def createFile(fileName, content):
    # Open a file
    fo = open(fileName, "wb")
    fo.write(content);

    fo.close()

def getSpecLocation():
    file_path = path.relpath("sample.doc")
    return file_path

createFile("main.cpp", generateCPPCode(readSpec(getSpecLocation())))
compileBinary()
runBinary()


# classes = natural_language_classifier.classify('e82f62x108-nlc-5131', 'As a user I want to add A and B?')
# print(json.dumps(classes, indent=2))
# 
# classes = natural_language_classifier.classify('e82f62x108-nlc-5131', 'As a user I want to divide A and B?')
# print(json.dumps(classes, indent=2))
# 
# classes = natural_language_classifier.classify('e82f62x108-nlc-5131', 'print output.')
# print(json.dumps(classes, indent=2))
# 
# natural_language_classifier = NaturalLanguageClassifierV1(
#   username='0d8af576-53ef-4feb-9511-7cb30a2b1728',
#   password='UbCAJZSXHbkA')
# 
# classes = natural_language_classifier.classify('004a12x110-nlc-3218', 'As a user I want to ask inputs.?')
# print(json.dumps(classes, indent=2))
# 
# classes = natural_language_classifier.classify('004a12x110-nlc-3218', 'As a user I want to add A and B?')
# print(json.dumps(classes, indent=2))
# 
# classes = natural_language_classifier.classify('004a12x110-nlc-3218', 'As a user I want to divide A and B?')
# print(json.dumps(classes, indent=2))
# 
# classes = natural_language_classifier.classify('004a12x110-nlc-3218', 'print output.')
# print(json.dumps(classes, indent=2))
