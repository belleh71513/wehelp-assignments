from flask import Flask, request, render_template, url_for, redirect, session, jsonify
from register_check import register, checkAccount, alterName
app = Flask(__name__, static_folder="static", static_url_path="/")
app.secret_key = "secret"

@app.route("/")
def index():
  if "username" in session:
    return redirect(url_for("member"))
  return render_template("index.html")

@app.route("/signup", methods=["POST"])
def signup():
  name=request.form["registerName"]
  username=request.form["registerUsername"]
  password=request.form["registerPassword"]
  checkUser = checkAccount(username)
  if not name or not username or not password:
    message = "姓名、帳號、密碼不得空白"
    return redirect(url_for("error", message=message))
  elif checkUser:
    message = "帳號已經被註冊"
    return redirect(url_for("error", message=message))
  else:
    register(name, username, password)
    return redirect(url_for("index"))

@app.route("/signin", methods=["POST"])
def signin():
  loginAcc = request.form["loginAcc"]
  loginPassword = request.form["loginPw"]
  checkLogin = checkAccount(loginAcc, loginPassword)
  if checkLogin :
    session["id"] = checkLogin[0]
    session["name"] = checkLogin[1]
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
    username = session["username"]
    return render_template("member.html", name=name, username=username)
  return redirect(url_for("index"))

@app.route("/error")
def error():
  message = request.args.get("message")
  return render_template("error.html", msg=message)

@app.route("/signout")
def signout():
  session.pop("username", None)
  return redirect(url_for("index"))

@app.route("/api/members")
def searchNameApi():
  if "uesername" in session:
    # 獲取前端傳送的值
    username = request.args.get("username")
    # 確認username是否存放於資料庫中
    getData = checkAccount(username)
    if getData :
      data = {
        "id" : getData[0],
        "name" : getData[1],
        "username" : getData[2]
      }
      return jsonify({"data":data})
    else:
      return jsonify({"data":None})
  return jsonify({"data":None})

@app.route("/api/member", methods=["POST"])
def alterNameApi():
  if "username" in session:
    # 獲取前端post的JSON型態資料
    getNameData = request.get_json()
    newName = getNameData["name"]
    username = session["username"]
    # 獲取資料庫中username資料
    getSqlData = checkAccount(username)
    if not newName :
      return jsonify({"error":True })
    else:
      # 修改name資料，並取得更新後的資料
      getNewData = alterName(newName, username)
      if getNewData:
        return jsonify({"ok":True })
  return jsonify({"error":True })


if __name__ == "__main__":
  app.run(port=3000)