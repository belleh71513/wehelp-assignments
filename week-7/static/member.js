
get = (e => document.querySelector(e))

const searchBtn = get("#searchBtn")
const alterBtn = get("#alterBtn")

function getData(){

  const searchInput = get("#searchInput").value;
  const searchVal = get("#searchVal");
  if (!searchInput){
    searchVal.innerText = "查詢欄位不得空白";
  }else{
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

}

function alterData(){

  const alterInput= get("#alterInput").value;
  const alterVal = get("#alterVal");
  if(!alterInput){
    alterVal.innerText = "更新欄位不得空白";
  }else{
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
}

searchBtn.addEventListener("click", getData);
alterBtn.addEventListener("click", alterData);

