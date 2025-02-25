from sqlite3 import complete_statement

import requests
import time
from creditional.constants import BOT_TOKEN_VALUE, API_URL_VALUE

API_URL = API_URL_VALUE
BOT_TOKEN = BOT_TOKEN_VALUE
TEXT = 'Ура! Классный апдейт!'
MAX_COUNTER = 20

offset = -2
counter = 0
chat_id: int


while counter < MAX_COUNTER:

    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')


    print(updates)
    time.sleep(1)
    counter += 1