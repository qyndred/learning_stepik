import requests

filename_in = r'C:\Users\Ririka1366\Downloads\dataset_3378_2.txt'
url = []

with open(filename_in, 'r') as import_file:
    for line in import_file:
        url.append(line.strip())

r = requests.get(*url)

print(len(r.text.splitlines()))