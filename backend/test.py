import requests

# https://requests.readthedocs.io/en/latest/user/advanced/#post-multiple-multipart-encoded-files

resp = requests.post("http://127.0.0.1:5000", files={'file': open('../model/3.png', 'rb')})

print(resp.json())
