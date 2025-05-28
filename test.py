import requests

print(requests.get('https://d453-76-22-92-25.ngrok-free.app/').text)

print(requests.get('https://d453-76-22-92-25.ngrok-free.app/gamelist').json())

print(requests.get('https://d453-76-22-92-25.ngrok-free.app/ditto').json())