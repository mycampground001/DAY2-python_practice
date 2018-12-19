from flask import Flask, render_template
import datetime as d ##as d를 하지 않으면 datetime.datetime.now() 이런식으로..
import random
app = Flask(__name__)

# month = d.datetime.today().month
# day = d.datetime.today().day

now = d.datetime.now()
month = now.month
day = now.day

@app.route("/")
def hello():
    return render_template("index.html") #templates 폴더안의 index.html을 불러옴

@app.route("/ssafy")
def ssafy():
    return "잘가 싸피~"

@app.route("/isitchristmas")
def christmas():


    if month==12 & day == 25:
         return "예~"
    else:
        return "아닙니다."

#variable routing
@app.route("/greeting/<string:name>")
def greeting(name):
    return f"{name}야 안녕~"

@app.route("/cube/<int:num>")
def cube(num):
    return f"{num*num*num}"

@app.route("/dinner")
def dinner():
    dinner = ["스팸","김혜자","신전"]
    image_urls = {
        "스팸":"http://www.nongaek.com/news/photo/201508/17224_9545_1614.jpg",
        "김혜자":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRewKpm1P-YVerSfXqtj0UI4BioHxEULzAhFVTs-k_s2klonXdj",
        "신전":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDNb6V87xvabymw_hPiXgrk69DZej8TPZxw7JzpZo3JlIcRESYwA"
    }
    menu = random.choice(dinner)
    menu_url = image_urls[menu]
    return render_template("dinner.html", menu=menu, dinner=dinner,menu_url=menu_url)

@app.route("/game")
def game():
    numbers= list(range(1,46))
    lotto = []

    while len(lotto)<6:
        num =random.choice(numbers)
        if not num in lotto:
            lotto.append(num)
            lotto.sort()
    return render_template("game.html",lotto=lotto)