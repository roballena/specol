def get(command):
    if command == 'cin':
        storage = 'int x =0;\n'
        cin = 'std::cin >> x;\n'
        return  storage + cin
    elif command == 'out_res':
        return "std::cout<<std::endl\n"
    else:
        return "//I'm still stupid, Teach me Master!\n"
    
    