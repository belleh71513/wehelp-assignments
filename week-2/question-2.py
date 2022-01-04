def avg(data):
# 請用你的程式補完這個函式的區塊

  salarySum = 0
  count = data["count"]
  for employees in data["employees"]:
    salarySum += employees.get('salary')


    # return salarySum
    # for salary in employees :
     # print(employees[salary])
  result = salarySum / count
  print(result)

avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
}) # 呼叫 avg 函式