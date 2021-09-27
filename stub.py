import requests
from datetime import date
base = "http://127.0.0.1:5000/"

response = requests.put(base + "updt/cpy/3", {
    "copy_id": "3",
    "draftid": "1"
})
#response = requests.get(base + "del/emp/5")
print(response.json())
