def get(command):
    if command[0] == 'cin':
        storage = 'int x =0;\n'
        cin = 'std::cin >> x;\n'
        return  storage + cin
    elif command[0] == 'cout':
        return "std::cout<<x<<std::endl;\n"
    elif command[0] == 'add':
        var1 = 'std::string var1 = "' + command[1][0] + '";\n'
        var2 = 'std::string var2 = "' + command[1][1] + '";\n'
        cout = "std::cout<< var1 << var2 << std::endl;\n"
        return var1 + var2 + cout
    else:
        return "//I'm still stupid, Teach me Master!\n"
    
    