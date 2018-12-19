phonebook = {
    # key : value
    "중국집":"022292",
    "초밥집":"1234-33",
    "한식집":"0201-22"
}

phonebook_2 = dict(중국집 = 1, 초밥집 = 2)

print(phonebook)
print(phonebook_2)

phonebook["분식집"] = "12131231"
print(phonebook["분식집"])

#1. 좋아하는 그룹 : key -  name, value - 나이
mylist = {"tnt":33,"aaa":22,"qqq":11,"lll":7}

# 2. idol이라는 dictionary 중첩된 형태의 dictionary
# idol - key : 그룹명, value : dictionary

idol = {
    "mylist" : {
        "tnt":33,
        "aaa":22,
        "qqq":11,
        "lll":7        
    },
    "uo" : {
        "weekend":40,
        "spencer":41,
        "aaron":44
    }
}

# dictionary 반복문
# for key in phonebook:
#     print(key , end=' ')
#     print(phonebook[key])

# key,value 출력 구문
# for a, b in phonebook.items():
#     print(a,b)

# for a in phonebook.values():
#     print(a)

# for key in phonebook.keys():
#     print(key)

