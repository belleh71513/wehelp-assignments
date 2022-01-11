import urllib.request as request
import json
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
  data = json.load(response)

newList = data["result"]["results"]
with open("data.csv", "w", encoding="utf-8") as file:

  for items in newList:
    stitle = items["stitle"]
    address = items["address"][5:8]
    longitude = items["longitude"]
    latitude = items["latitude"]
    fileStr = items["file"].lower()
    fileUrlList = fileStr.split(".jpg",1)
    firstImgURL = fileUrlList[0] + ".jpg"

    file.write(stitle +","+ address +","+ longitude +","+ latitude +","+ firstImgURL + "\n")


