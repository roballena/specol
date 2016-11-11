from watson_developer_cloud import NaturalLanguageClassifierV1
from construct_cpp import generateIOHeader, generateMainMethod
from cpp_command_factory import get

natural_language_classifier = NaturalLanguageClassifierV1(
  username='0d8af576-53ef-4feb-9511-7cb30a2b1728',
  password='UbCAJZSXHbkA')

statements = {'As a user I want to ask inputs.?', 'print output.','asdfasdfasdfasd',}

def getCommand(statement):
    classes = natural_language_classifier.classify('e82f62x108-nlc-5131', statement)
    return classes["top_class"]
    
def generateCPPCode(codes):
    lineOfCodes = ''
    for code in codes:
        lineOfCodes = lineOfCodes + get(getCommand(code))
    file_output = generateIOHeader() + generateMainMethod(lineOfCodes)
    print file_output
    return file_output


def createFile(fileName, content):
    # Open a file
    fo = open(fileName, "wb")
    fo.write(content);

    fo.close()

createFile("main.cpp", generateCPPCode(statements))


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
