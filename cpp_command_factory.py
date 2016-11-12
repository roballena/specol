def get(command):
    if command[0] == 'cin':
        storage = 'int x =0;\n'
        cin = 'std::cin >> x;\n'
        return  storage + cin
    elif command[0] == 'out_res':
        return "std::cout<<x<<std::endl;\n"
    else:
        return "//I'm still stupid, Teach me Master!\n"
    
    