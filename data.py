import requests

from random import *

amount = randint(10, 50)

response = requests.get(url="https://opentdb.com/api.php?amount=20&type=boolean")
if response.status_code != 200:
    response.raise_for_status()
data = response.json()
