from flask import Flask, render_template
from user import Users

@app.route('/users')
def index():
    users = users.get_all()
    print(users)
    return render_template("read.html", all_users = users)


@app.route('/users/new')

@app.route('/users/4')

@app.route('/users/4/edit')