import json
import requests
import csv
from datetime import datetime

r = requests.get('http://192.168.0.144/temp')
data = dict(json.loads(r.text.replace("'", '"')))

#data = {'temp': 28.0, 'hum': 31.0}



while int(datetime.now().strftime("%H")) != 10:
    if int(datetime.now().strftime("%M")) % 5 == 0 and int(datetime.now().strftime("%S")) == 0:
        r = requests.get('http://192.168.0.144/temp')
        data = dict(json.loads(r.text.replace("'", '"')))

        with open('c:/Users/ИВАН/Desktop/egg.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([data['temp'], data['hum'], datetime.now()])
            print([data['temp'], data['hum'], datetime.now()])



