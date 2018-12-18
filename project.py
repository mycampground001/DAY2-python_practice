with open("ssafy.txt","w") as file:
    file.write("1\n2\n3\n4\n5\n6\n7\n8\n9\n")

with open("ssafy.txt","r") as file:
    lines=file.readlines()
    #print(lines)
    print("len= ",len(lines))
    #Search
    


    cnt=1
    for i in range(len(lines)//2):
            aaa=lines[i]
            lines[i]=lines[len(lines)-cnt]
            lines[len(lines)-cnt]=aaa
            cnt+=1

    print(lines)

with open("ssafy.txt","w") as file:
    for line in lines:
        file.write(line)


r_lines=reversed(lines)
for line in r_lines:
    print(line.strip('\n'))


# ================== 구구단 출력 =======================
for i in range(1,10):
    print("aaaa \t")