import random
"""
난이도* 1. 지역(location)은 몇개 있나요?
출력예시)
4
난이도** 2. python standard library에 'requests'가 있나요?
출력예시)
false
난이도** 3. dj1반의 반장의 이름을 출력하세요.
출력예시)
박성민
난이도*** 4. ssafy에서 배우는 언어들을 출력하세요.
출력 예시)
python
web
난이도*** 5 ssafy dj2의 강사와 매니저의 이름을 출력하세요.
출력 예시)
junho
pro2
난이도***** 6. framework들의 이름과 설명을 다음과 같이 출력하세요.
출력 예시)
flask는 micro이다.
django는 full-functioning이다.
난이도***** 7. 오늘 당번을 뽑기 위해 groups의 3조 중에 한명을 랜덤으로 뽑아주세요.
출력예시)
오늘의 당번은 고병석
"""

ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "dj1":  {
            "lecturer": "tak",
            "manager": "pro1",
            "class president": "박성민",
            "groups": {
                "1조": ["강신욱", "윤영우", "이민교", "유창오", "황여진", "김민경"],
                "2조": ["노승만", "이재찬", "이주호", "김예지", "유지원"],
                "3조": ["이민지", "김희윤", "박성민", "조인정", "김슬기", "고병석"],
                "4조": ["임동명", "김승훈", "정상영", "정태현", "한단비", "김동민"]
            }
        },
        "dj2": {
            "lecturer": "junho",
            "manager": "pro2"
        }
    }
}


for key, name in ssafy.items():
    #=========Q1==========
    if key == "location":
        Q1 = len(name)

    #=========Q2==========
    elif key == "language":
        for lang, val in name.items():
            if lang == "python":
                for lang_, val_ in val.items():
                    if lang_ == "python standard library":
                        if "request" in val_:
                            Q2 = "True"
                        else:
                            Q2 = "false"

Q3 = ssafy["classes"]["dj1"]["class president"]

Q4 = ""
for langs in ssafy["language"]:
    Q4 += f"{langs}\n"

Q5 = ""
for name in ssafy["classes"]["dj2"].values():
    Q5 += f"{name}\n"

Q6 = ""
for keys,val in ssafy["language"]["python"]["frameworks"].items():
    Q6 += f"{keys}는 {val}이다.\n"

for group,name in ssafy["classes"]["dj1"]["groups"].items():
    if group == "3조":
        Q7 = random.choice(name)

print("=====Q1. 지역은 몇 개 인가요?=====")
print(f"{Q1}개 입니다.\n")

print("=====Q2. python standard libary에 requests가 있는지?=====")
print(f"{Q2}\n")


print("=====Q3. 반장의 이름은?=====")
print(f"{Q3}\n")


print("=====Q4. 배우는 언어?=====")
print(Q4)


print("=====Q5. ssafy dj2의 강사와 매니저의 이름을 출력하세요.=====")
print(Q5)


print("=====Q6. framework들의 이름과 설명을 다음과 같이 출력하세요.=====")
print(Q6)

print("=====Q7. 3조 중 한명 ======" )
print(f"jintian {Q7}")