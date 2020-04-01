import requests

URL = "https://covid19.th-stat.com/api/open/today"

req = requests.get(URL)

data = req.json()
print(data)

csv = f""",ข้อมูลอัปเดต เมื่อ {data['UpdateDate']}
จำนวนคนที่<b>ถูกตรวจและมีผลบวก</b>เพิ่มเติม,{data['NewConfirmed']}
จำนวนผู้ป่วยที่<b>เสียชีวิต</b>ในวันนี้,{data['NewDeaths']}
"""

print(csv)

with open("./data/covid-19-latest.csv", "w") as f:
    f.write(csv)