import os


def compileBinary():
    os.system('g++ main.cpp -o main')
    
def runBinary():
    os.system('main.exe')