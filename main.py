from flask import Flask, render_template, jsonify, request
import pymysql

app = Flask(__name__)
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='ai_college_web', charset="utf8")
cursor = db.cursor()


@app.route("/page", methods=["GET"])
def hello():
    return render_template('index.html')


@app.route("/student", methods=["GET"])
def get_students():
    sql = "select * from student"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.commit()
    students = []
    for result in results:
        students.append({
            'id': result[0],
            'name': result[1],
            'age': result[2]
        })
    return jsonify(students)


@app.route("/student", methods=["POST"])
def save_student():
    server_name = request.form["name"]
    server_age = request.form["age"]
    sql = "insert into student (name, age) values ('%s', %s)" % (server_name, server_age)
    cursor.execute(sql)
    db.commit()
    return "OK"


@app.route("/student", methods=["PUT"])
def update_student():
    server_id = request.form["id"]
    server_name = request.form["name"]
    server_age = request.form["age"]
    sql = "update student set name = '%s', age = %s where id = %s" % (server_name, server_age, server_id)
    cursor.execute(sql)
    db.commit()
    return "OK"


@app.route("/student", methods=["DELETE"])
def delete_student():
    server_id = request.args.get("id")
    sql = "delete from student where id = %s" % server_id
    cursor.execute(sql)
    db.commit()
    return "OK"


if __name__ == "__main__":
    app.run(debug=True)