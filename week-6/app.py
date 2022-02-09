from flask import Flask, request, render_template, url_for, redirect, session
from register_check import register, loginConfirmation, checkUserExist
app = Flask(__name__, static_folder="static", static_url_path="/")
app.secret_key = "secret"

@app.route("/")
def index():
  if "username" in session:
    return redirect(url_for("member"))
  return render_template("index.html")

@app.route("/signin", methods=["POST"])
def signin():
  loginAcc = request.form["loginAcc"]
  loginPassword = request.form["loginPw"]
  loginCheck = loginConfirmation(loginAcc, loginPassword)

  if loginCheck :
    session["name"] = loginCheck[1]
    session["username"] = loginAcc
    session["password"] = loginPassword
    return redirect(url_for("member"))
  elif not loginAcc or not loginPassword:
    message="請輸入帳號、密碼"
    return redirect(url_for("error", message=message))
  else:
    message="帳號、密碼輸入錯誤"
    return redirect(url_for("error", message=message))

@app.route("/member/")
def member():
  if "username" in session:
    name = session["name"]
    return render_template("member.html", name=name)
  return redirect(url_for("index"))

@app.route("/error")
def error():
  message = request.args.get("message")
  return render_template("error.html", msg = message)

@app.route("/signout")
def signout():
  session.pop("username", None)
  return redirect(url_for("index"))

@app.route("/signup", methods=["POST"])
def signup():
  name=request.form["registerName"]
  username=request.form["registerUsername"]
  password=request.form["registerPassword"]
  checkUser = checkUserExist(username)
  if not name or not username or not password:
    message = "姓名、帳號、密碼不得空白"
    return redirect(url_for("error", message=message))
  elif checkUser:
    message = "帳號已經被註冊"
    return redirect(url_for("error", message=message))
  else:
    register(name, username, password)
    return redirect(url_for("index"))

if __name__ == "__main__":
  app.run(port=3000)