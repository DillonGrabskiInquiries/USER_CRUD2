from flask import Flask, render_template
from user import Users

@app.route('/users')
def index():
    users = users.get_all()
    print(users)
    return render_template("read.html", all_users = users)


@app.route('/users/new')
def index():
    users = users.get_all()
    print(users)
    return render_template("create.html", all_users = users)

@app.route('/users/4')
def index():
    users = users.get_all()
    print(users)
    return render_template("read.html", all_users = users)

@app.route('/users/4/edit')
def index():
    users = users.get_all()
    print(users)
    return render_template("read.html", all_users = users)