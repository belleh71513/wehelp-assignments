from email import message
import pstats
from flask import Flask, request, render_template, url_for, redirect, session
from markupsafe import re

app = Flask(__name__)

app.secret_key = "secret"

@app.route("/")
def index():
  if "user" in session:
    return redirect(url_for("member"))
  return render_template("index.html")

@app.route("/signin", methods=["POST"])
def signin():
  account = request.form["acc"]
  password = request.form["pw"]
  if account == "test" and password == "test":
    session["user"] = account
    return redirect(url_for("member"))
  elif len(account) == 0 or len(password) == 0:
    return redirect(url_for("error", message="請輸入帳號、密碼"))
  else:
    return redirect(url_for("error", message="帳號、密碼輸入錯誤"))

@app.route("/member")
def member():
  if "user" in session:
    return render_template("member.html")
  return redirect(url_for("index"))

@app.route("/error")
def error():
  message = request.args.get("message", "")
  return render_template("error.html", msg = message)

@app.route("/signout")
def signout():
  session.pop("user", None)
  return redirect(url_for("index"))







if __name__ == "__main__":
  # app.debug=True

  app.run(port=3000)