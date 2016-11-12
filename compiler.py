import os
from os import path

def compileBinary():
    print "Compiling c++ code"
    os.system('g++ main.cpp -o main.exe')
    print 'Code compilation done!\n'
    file_path = path.relpath("main.exe")
    print 'Output file: ' + file_path
    
def runBinary():
    print 'Running main.exe'
    os.system('main.exe')
    print 'Program execution done!\n'