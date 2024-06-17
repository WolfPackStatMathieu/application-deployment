import requests

url = "https://toto.kub.sspcloud.fr/proxy/8000/predict?sex=female&age=29&fare=16.5&embarked=S"

response = requests.get(url)
if response:
    print("Success!")
    print(response.content)
else:
    raise Exception(f"Non-success status code: {response.status_code}")