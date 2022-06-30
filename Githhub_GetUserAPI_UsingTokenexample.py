import requests
from requests.structures import CaseInsensitiveDict

url = "https://api.github.com/user"
token= "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"
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer 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"
print(type(headers))


resp = requests.get(url, headers=headers)

print(resp.status_code)