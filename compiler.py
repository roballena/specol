import os


def compileBinary():
    print "Compiler c++ code\n"
    os.system('g++ main.cpp -o main')
    print 'Code compilation done!\n'
    
def runBinary():
    print 'Running main.exe'
    os.system('main.exe')
    print 'Program execution done.\n'