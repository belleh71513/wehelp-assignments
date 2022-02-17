const searchBtn = document.querySelector("#searchBtn")
const alterBtn = document.querySelector("#alterBtn")

function getData(){

  const searchInput = document.querySelector("#searchInput").value
  const searchVal = document.querySelector("#searchVal")
  fetch(`http://127.0.0.1:3000/api/members?username=${searchInput}`,)
  .then((response) => {
    if(!response.ok){
      throw new Error(response.statusText);
    }
    return response.json();
  })
  .then((data) => {
    if(data["data"] !== null){
      let name = data["data"]["name"];
      let username = data["data"]["username"];
      searchVal.innerText = `${name}(${username})`;
    }
    else{
      searchVal.innerText = "查無此會員";
    }
  })
}

function alterData(){

  const alterInput= document.querySelector("#alterInput").value
  const alterVal = document.querySelector("#alterVal")
  fetch("http://127.0.0.1:3000/api/member",{
    method: "POST",
    headers:{
      "Accept": "application/json",
      "Content-Type": "application/json"
    },
    body:JSON.stringify({
        "name":alterInput
    })
  })
  .then(response => {
    return response.json();
    })
  .then(data => {
    if(data["ok"]){
      alterVal.innerText = "更新成功";
    }
    if(data["error"]){
      alterVal.innerText = "更新失敗";
    }
  })
}

searchBtn.addEventListener("click", getData);
alterBtn.addEventListener("click", alterData);

