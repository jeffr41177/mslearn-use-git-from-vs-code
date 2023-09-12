# name = input('Enter your name: ')
# print(name)


# print('What is your name?')
# name = input()
# print(name)

# x = int(input('Enter a number: '))
# print(type(x))

# x = 5
# print('The variable x contains the number ', x)


# first_number = int(input('Type the first number: ')) 
# second_number = int(input('Type the second number: '))
# print("The sum is:", first_number + second_number)
# print(first_number)

from string import Template

import requests

url = "https://api.collection.cooperhewitt.org/rest/?method=cooperhewitt.search.objects&query=clock%20radio&page=1&per_page=100&access_token=19cfa18706157340155372a7d67cf21d"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))