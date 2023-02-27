import requests

# Request the HTML content of the website and store it in a variable to create a image file

# png = requests.get('https://imgs.xkcd.com/comics/jealousy.png')

# Create a file and write the content of the request to it
# with open('jealousy.png', 'wb') as f:
   # f.write(r.content)

# Status code 200 means the request was successful
# print(r.status_code)
# print(r.ok)
# print(r.headers)


payload = {'username': 'pepe', 'password': 'testing'}
# r = requests.get('https://httpbin.org/get', params=payload)
# r = requests.post('https://httpbin.org/post', data=payload)

# r = requests.get('https://httpbin.org/basic-auth/pepe/testing', 
#                  auth=('pepe', 'testing'))

# Timeout in seconds (3 seconds) if the server doesn't respond
r = requests.get('https://httpbin.org/delay/2', timeout=3)

# print(r.text)
# print(r.url)

# To get the JSON response from the request
# print(r.json()['form'])

print(r)

