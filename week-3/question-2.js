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
  console.log(arrText)

  for(let i=0 ; i<attLegth ; i++){
    arrImg.push(attractions[i]["file"].toLowerCase().split("jpg", 1) + "jpg")
  };


  for(let i=0 ; i<8 ; i++){
  let body = document.querySelector("body");

  let divIntro = document.createElement("div")
  divIntro.className = "introduce";

  let divItemgroup = document.createElement("div");
  divItemgroup.className = "item-group"

  let divItem = document.createElement("div");
  divItem.className = "item"

  let divPic = document.createElement("div");
  divPic.className = "pic"

  let img = document.createElement("img");
  img.src = arrImg[i]

  let divText = document.createElement("div");
  divText.className = "text";
  divText.innerText = arrText[i]

  body.appendChild(divIntro);
  divIntro.append(divItemgroup);
  divItemgroup.append(divItem);
  divItem.append(divPic);
  divItem.append(divText);
  divPic.append(img);
  }



}

