def generateIOHeader():
    return '#include <iostream>\n'

def generateMainMethod(statement):
    opening ='int main(){\n'
    closing = '}'
    generatedCode = opening + statement + closing
    return generatedCode
    