       

kanye_url = 'https://api.kanye.rest'


# quotes = []
# for i in range(10):
    
#     response = httpx.request(method='GET', url=kanye_url)
#     response.raise_for_status()
#     data = response.json()
#     quotes.append(data['quote'])
    
# print(quotes)

iss_url = 'http://api.open-notify.org/iss-now.json'


r = httpx.request(method='GET', url=iss_url)
r.raise_for_status()

data = r.json()

print(data.get('iss_position').get('longitude'))