with open("new2.txt","r") as file:
    print(type(file))
    for line in file:
        print(line.strip('\n'))