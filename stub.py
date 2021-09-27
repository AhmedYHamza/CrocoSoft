import requests
from datetime import date
base = "http://127.0.0.1:5000/"

response = requests.put(base + "hist/3", {
    "type": "doc"
})
#response = requests.get(base + "/del/doc/7")
print(response.json())
