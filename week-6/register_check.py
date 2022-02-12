import mysql.connector
from mysql.connector import pooling
mydb_connection_pool = mysql.connector.pooling.MySQLConnectionPool(
  pool_name = "mypool",
  pool_size = 3,
  pool_reset_session = True,
  host = "localhost",
  user = "root",
  password = "password",
  database = "week6"
)
mydb = mydb_connection_pool.get_connection()
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









