import requests
from datetime import date
base = "http://127.0.0.1:5000/"

# response = requests.put(base + "/updt/doc/7", {
#    "doc_id": "7",
#    "is_from_outside": "1",
#    "doc_status": "recieved",
#    "date_created": "2021-09-27",
#    "date_modified": "2021-09-27",
#    "reciet_date": "2021-09-27",
#    "reciet_num": 1557,
# })
#response = requests.get(base + "/del/doc/7")
print(response.json())
