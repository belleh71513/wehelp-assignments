from hashlib import new
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
  cursor.execute(sql, (name, username, password))
  mydb.commit()
  # cursor.close()
  # mydb.close()

# 登入確認 & 查詢資料
def checkAccount(username, password=None):
  if password is None:
    cursor.execute("SELECT * FROM memberSystem WHERE username=%s",(username,))
    checkUsername = cursor.fetchone()
    return checkUsername
  else:
    cursor.execute("SELECT * FROM memberSystem WHERE username=%s AND password=%s",( username, password))
    checkLogin = cursor.fetchone()
    return checkLogin

def alterName(newName, username):
  # 以username 唯一值特性作為where條件，set相對應name資料
  cursor.execute("UPDATE memberSystem SET name=%s WHERE username=%s ",(newName, username))
  mydb.commit()
  # 檢查資料庫中newname是否存在
  checkNewName = checkAccount(username)
  # 確認name是否更改為前端過來的值
  if checkNewName[1] == newName:
    return True














