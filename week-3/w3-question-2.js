
//取得網址，並送出請求讀取JSON資料
let src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json" ;
let request = new XMLHttpRequest();
request.open('get', src);
//request.responseType = 'json';
request.send();

request.onload = function() {
  //將JSON轉成物件格式
  let data = JSON.parse(this.responseText);
  //取得景點圖片、景點名稱
  let arrImg = [] ;
  let arrText = [];
  let strImg = "" ;
  let attractions = data["result"]["results"] ;
  let attLegth = attractions.length ;
  //取得景點名稱(一大串字串)並於後面加上',' 以利後續切割成陣列
  for(let i=0 ; i<attLegth ; i++){
    strImg += attractions[i]["stitle"] + ",";
  };
  //取得景點名稱陣列 : 將字串切割並push進陣列中
  arrText = strImg.split(",")
  /*取得景點圖片網址(一大串字串)並將字串轉成小寫 利用"jpg"進行切割成1個陣列 再將"jpg"加回原網址之中
  */
  for(let i=0 ; i<attLegth ; i++){
    arrImg.push(attractions[i]["file"].toLowerCase().split("jpg", 1) + "jpg")
  };

  //取得body標籤
  let body = document.querySelector("body");
  //建立div標籤並加上class名稱
  let divCon = document.createElement("div");
  divCon.className = "container";

  let divWrap = document.createElement("div");
  divWrap.className = "wrap";

  body.appendChild(divCon);
  divCon.append(divWrap);


  for(let i=0 ; i<8 ; i++){
  let divItem = document.createElement("div");
  divItem.className = "item"

  let divPic = document.createElement("div");
  divPic.className = "pic"

  let img = document.createElement("img");
  img.src = arrImg[i]

  let divItemText = document.createElement("div");
  let textP = document.createElement("p")
  divItemText.className = "itemText";
  textP.innerText = arrText[i]


  divWrap.append(divItem);
  divItem.append(divPic);
  divItem.append(divItemText);
  divItemText.append(textP);
  divPic.append(img);
  }



}

