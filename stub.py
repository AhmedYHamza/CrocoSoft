import requests
from datetime import date
base = "http://127.0.0.1:5000/"

response = requests.put(base + "transdoc", {
    "circulation_id": "8",
    "source_id": "3",
    "source_type": "doc",
    "emp_ssn": "4",
    "date_modified": "2021-09-27"
})
#response = requests.get(base + "/del/doc/7")
print(response.json())
