import httpx

# kanye_url = 'https://api.kanye.rest'

# frases = []

# for _ in range(10):
#     # response = httpx.request(method='GET', url=kanye_url)
#     response = httpx.get(url=kanye_url)
#     response.raise_for_status() # Revisar si la petición se realizó correctamente
#     data:dict = response.json()
#     frases.append(data.get('quote'))

# for i in frases:
#     print(i)

# theOneUrl = 'https://the-one-api.dev/v2'

# endpoint = '/character'
# key = 'pG_L0zZLBAb0FjFwPicV'

# head = {
#     'Authorization': f'Bearer {key}'
# }

# parametros = {
#     'limit': 2
# }

# final_url = f'{theOneUrl}{endpoint}'

# r = httpx.request(method='GET', url=final_url, headers=head, params=parametros)
# r.raise_for_status()

# data = r.json()

# # print(data)

# raza = data['docs'][0]['race']

# print(raza)


space_url = 'http://api.open-notify.org/astros.json'

r = httpx.get(url=space_url)
r.raise_for_status()

data = r.json()

print(data)