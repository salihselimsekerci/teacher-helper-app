from flask import Flask, render_template, request, redirect, url_for
from .models import db, Student, Performance

@app.route("/")
def home():
    students = Student.query.all()
    return render_template("home.html", students=students)

@app.route("/add_student", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        new_student = Student(name=name, email=email)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_student.html")
