let src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json" ;
let request = new XMLHttpRequest();
request.open('get', src);
// request.responseType = 'json';
request.send();
request.onload = function() {
  let data = JSON.parse(this.responseText);
  let arrImg = [] ;
  let arrText = [];
  let strImg = "" ;
  attractions = data["result"]["results"] ;
  attLegth = attractions.length ;
  for(let i=0 ; i<attLegth ; i++){
    strImg += attractions[i]["stitle"] + ",";
  };
  arrText = strImg.split(",")

  for(let i=0 ; i<attLegth ; i++){
    arrImg.push(attractions[i]["file"].toLowerCase().split("jpg", 1) + "jpg")
  };

  let body = document.querySelector("body");

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
  divItemText.className = "itemText";
  divItemText.innerText = arrText[i]


  divWrap.append(divItem);
  divItem.append(divPic);
  divItem.append(divItemText);
  divPic.append(img);
  }



}

