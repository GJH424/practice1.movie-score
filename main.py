from flask import Flask, render_template, jsonify, request
import pymysql

app = Flask(__name__)
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='ai_college_web', charset="utf8")
cursor = db.cursor()


@app.route("/", methods=["GET"])
def print_hi():
    return "OK"

@app.route("/page", methods=["GET"])
def mainPage():
    return render_template('index.html')

# 자료 불러오기
@app.route("/practice", methods=["GET"])
def get_movies():
    cursor.execute("select * from practice")
    results = cursor.fetchall()
    movies = []
    for result in results:
        movies.append({
            "id": result[0],
            "name": result[1],
            "score": result[2]
        })
    return jsonify(movies)

#평점 저장
@app.route("/practice", methods=["POST"])
def save_score():
    name = request.form['name']
    score = request.form['score']
    cursor.execute(f"insert into practice (name, score) values ('{name}', {score})")
    db.commit()
    return "POST"

#목록 제거
@app.route("/practice", methods=["DELETE"])
def del_score():
    cursor.execute(f"delete from practice")
    db.commit()
    return "DELETE"

if __name__ == "__main__":
    app.run(debug=True)