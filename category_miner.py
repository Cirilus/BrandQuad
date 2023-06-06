import json

import requests

req = requests.get("https://apteka-ot-sklada.ru/api/category")
js = req.text

js = json.loads(js)

with open("category.json", "w") as file:
    json.dump(js, file, ensure_ascii=False)
