import requests
from datetime import date
base = "http://127.0.0.1:5000/"

# response = requests.put(base + "add/emp", {
#    "ssn": "5",
#    "emp_name": "hamza",
#    "job_tite": "frontend engineer",
#    "email": "hamza@gmail.com"
# })
#response = requests.get(base + "del/emp/5")
print(response.json())
