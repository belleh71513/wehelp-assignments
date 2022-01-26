# Assignment - Week 5

## 要求三 : SQL CRUD
### 利用要求二建立的資料庫和資料表，寫出能夠滿足以下要求的 SQL 指令：

1.使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和
password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。
![](https://s3.bmp.ovh/imgs/2022/01/22a615620c91629a.png)
2.使用 SELECT 指令取得所有在 member 資料表中的會員資料。
![](https://s3.bmp.ovh/imgs/2022/01/22a615620c91629a.png)
3.使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由
近到遠排序。
![](https://i.imgur.com/NmAIxEX.png)
4.使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，
由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )
![](https://i.imgur.com/tfCiFPH.png)
5.使用 SELECT 指令取得欄位 username 是 test 的會員資料。
![](https://i.imgur.com/rnGTHp9.png)
6.使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
![](https://i.imgur.com/EvwtzoD.png)
7.使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位
改成 test2。
![](https://i.imgur.com/uGrK7cn.png)

## 要求四 : SQL Aggregate Functions
### 利用要求二建立的資料庫和資料表，寫出能夠滿足以下要求的 SQL 指令：
1.取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
![](https://i.imgur.com/47ppHt9.png)
2.取得 member 資料表中，所有會員 follower_count 欄位的總和。
![](https://i.imgur.com/nWpEBwe.png)
3.取得 member 資料表中，所有會員 follower_count 欄位的平均數。
![](https://i.imgur.com/9e7y1bU.png)

## 要求五 : SQL JOIN
1.在資料庫中，建立新資料表，取名字為 message。資料表中必須包含以下欄位設定：
![](https://i.imgur.com/8GkpuKV.png)
2.使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。
![](https://i.imgur.com/1zlnTqS.png)
3.使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有
留言，資料中須包含留言者會員的姓名。
![](https://i.imgur.com/7VfpVy7.png)





