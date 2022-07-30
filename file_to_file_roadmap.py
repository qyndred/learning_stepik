import requests
import re

filename_in = r'C:\Users\Ririka1366\Downloads\dataset_3378_3 (1).txt'
url = ''

with open(filename_in, 'r') as import_file:
    for line in import_file:
        url += line.strip()

while not requests.get(url).text.startswith('We'):
    next_url = re.sub(r'\d{6}.txt', requests.get(url).text, url)
    url = next_url
    print(requests.get(url).text)