import requests
import json 


response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
# responding to the website you put in 

for data in response.json()['items']:
    if data ['answer_count'] == 0: # shows all the titles and tables 
        print(data)
        print(data['link'] ) # shows you the website link
    else:
        print("skipped")
    print()