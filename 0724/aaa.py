import requests
from pprint import pprint as print

dummy_data = []

# 무작위 유저 정보 요청 경로
for i in range(1, 11):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'

    response = requests.get(API_URL)

    parsed_data = response.json()
    
    if (80 > float(parsed_data['address']['geo']['lat']) > -80) and (80 > float(parsed_data['address']['geo']['lng']) > -80):
        dummy_data.append({'company' : parsed_data['company']['name'], 'lat' : parsed_data['address']['geo']['lat'], 'lng' : parsed_data['address']['geo']['lng'], 'name' : parsed_data['name']})



print(dummy_data)
print(len(dummy_data))