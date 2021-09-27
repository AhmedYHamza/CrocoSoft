import requests
from datetime import date
base = "http://127.0.0.1:5000/"

# response = requests.put(base + "add/doc", {
#    "doc_id": "6",
#    "is_from_outside": "1",
#    "doc_status": "recieved",
#    "date_created": "2021-09-27",
#    "date_modified": "2021-09-27"
# })
response = requests.get(base + "get/doc/1")
print(response.json())
