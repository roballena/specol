import os

def compileBinary():
    print "Compiling c++ code\n"
    os.system('g++ main.cpp -o main.exe')
    print 'Code compilation done!\n'
    
def runBinary():
    print 'Running main.exe'
    os.system('main.exe')
    print 'Program execution done.\n'