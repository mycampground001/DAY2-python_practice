# file = open("new.txt","w")
# file.write("글써졌나?")
# file.close()

# 1. 파일 생성

with open("new1.txt","w") as file:
    '''
    파이썬에서 with는 컨택스트 매니저라고 부른다.
    with 블록내에서 파일을 조작하고,
    블록이 끝나게 되면 파일이 닫히게 된다.
    '''
    file.write("글 또 쓰자")

# 2. 파일 읽기
with open("new.txt","r") as file:
    line = file.read()
    print(line)

# 3. 파일 여러 줄 쓰기
with open("new2.txt","w") as file:
    for line in range(55):
        file.write(f"{line}번째 줄입니다.\n")

# 4. 파일 여러줄 읽기
with open("new2.txt","r") as file:

    # while 1:
    #    line = file.readline()
    #    if line == '':
    #        break
    #    print(line)

    lines=file.readlines()
    print(lines)
    print(len(lines))
    print(type(lines))
    # lines 리스트를 출력해주세요.
    for line in lines:
        print(line)
