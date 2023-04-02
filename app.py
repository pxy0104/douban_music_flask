from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/index')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/music')
def music():
    if request.method == "GET":
        page = int(request.args.get('page'))
        print(page)
        print("get")
    else:
        page = int(request.form.get('page'))
        print(page)
        print("post")
    if page == '':
        page = 1
    datalist = []
    con = sqlite3.connect("music.db")
    cur = con.cursor()

    sql = "select * from music247 LIMIT " + str((int(page) - 1) * 10) + " , 10"
    # sql = "select * from movie250 LIMIT 1,4"
    data = cur.execute(sql)
    # print(data)
    for i in data:
        datalist.append(i)
    cur.close()
    con.close()
    return render_template('music.html', musics=datalist, page=page)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/category')
def category():
    return render_template('category.html')

@app.route('/score')
def score():
    score=[] #音乐评分
    num = [] #相同评分的数量
    conn = sqlite3.connect('music.db')
    cur = conn.cursor()
    sql = "select score,count(score) from music247 group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(item[0])
        num.append(item[1])
    return render_template("score.html",score=score,num=num)


@app.route('/wordcloud')
def wordcloud():
    return render_template('wordcloud.html')

if __name__ == '__main__':
    app.run()
