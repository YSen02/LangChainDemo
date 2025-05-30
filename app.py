from flask import Flask, request, render_template, redirect, session, url_for

app = Flask(__name__)
app.debug = True
app.secret_key = "hxd123"

user_data = {
    "hxd": "123",
    "lw": "123"
}

score = {
    "hxd": {"chinese": 60, "math": 78, "english": 70},
    "lw": {"chinese": 80, "math": 68, "english": 73}
}


@app.route("/")
def main():
    return redirect("/login")


@app.route("/index")
def index():
    try:
        user = session['user_info']
    except:
        user = ""
    if not user:
        url = url_for('ll')      # 反向解析
        return redirect(url)
    print(score[user])
    return render_template("index.html", user=user, dic=score[user])


@app.route("/login", methods=['GET', 'POST'], endpoint="ll")
def login():
    # get请求的数据放在request.query_string
    # post请求的数据放在request.form
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        session['user_info'] = username
        # if username == "hxd" and password == "123":
        if username in user_data:
            if user_data[username] == password:
                return redirect("/index")
            else:
                return render_template("login.html", Error="密码错误！")
        else:
            return render_template("login.html", Error="没有该用户！")


if __name__ == '__main__':
    app.run()
