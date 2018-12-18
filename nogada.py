import os

# SSAFY_지원자 폴더로 들어가고

# SSAFY지원자 폴더로 들어가고

# 내용 모두 출력

os.chdir(r'SSAFY_지원자')
os.chdir(r'SSAFY지원자')
print(os.getcwd())
files = os.listdir()
for file in files:
    os.rename(file,file.replace("SAMSUNG","SSAFY"))