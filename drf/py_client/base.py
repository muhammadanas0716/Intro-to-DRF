import requests

endpoint = "http://localhostuhb      :8000"

get_response = requests.get(endpoint, json={"query" : "Hello World"}) # HTTP Request

print(get_response.text)
print(get_response.status_code)