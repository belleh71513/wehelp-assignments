import mysql.connector
mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "password",
  database = "week6"
)
cursor = mydb.cursor(buffered=True)

# 註冊帳號
def register(name, username, password):
  sql = "INSERT INTO memberSystem(name, username, password) VALUES (%s, %s, %s)"
  cursor.execute(sql, (name, username, password,))
  mydb.commit()
  # cursor.close()
  # mydb.close()

# 登入確認
def loginConfirmation(username, password):
  cursor.execute("SELECT * FROM memberSystem WHERE username=%s AND password=%s",( username, password,))
  loginAccountCheck = cursor.fetchone()
  return loginAccountCheck

# 檢查帳號是否重複
def checkUserExist(username):
  cursor.execute("SELECT username FROM memberSystem WHERE username=%s",(username,))
  checkAccount = cursor.fetchone()
  if checkAccount:
    return True

# def checkName(name):
#   cursor.execute("SELECT name FROM memberSystem WHERE name=%s",(name,))
#   checkName = cursor.fetchone()
#   if checkName:
#     print(checkName[0])



# def register(**kwargs):
#   sql = "INSERT INTO memberSystem(name, username, password) VALUES (%s, %s, %s)"
#   cursor.execute(sql, (name=name, username=username, password=password,))
#   mydb.commit()
#   cursor.close()
#   mydb.close()

# def checkUserExist(**kwargs):
#   cursor.execute("SELECT username FROM memberSystem WHERE username=%s",(username,))
#   checkAccount = cursor.fetchone()
#   if checkAccount:
#     return True







