from requests import get
from json import loads

api = get('http://127.0.0.1:5000/mostrar_tudo')
print(loads(api.content))
