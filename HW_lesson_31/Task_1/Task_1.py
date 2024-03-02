#Task 1
"""
Robots.txt
Download and save to file robots.txt from wikipedia, twitter websites etc. 
"""
import requests


SITES = ["https://twitter.com/robots.txt", "https://www.facebook.com/robots.txt", "https://en.wikipedia.org/robots.txt"]

for site in SITES:
    response = requests.get(site)
    if response.status_code != 200:
        print(f"Request error. Status code: {response.status_code}")
    else:
        try:
            with open(f'{site.split("/")[-2]}_robots.txt', 'w', encoding='utf-8') as file:
                file.write(response.text)
        except Exception as e:
            print(f"Error writing to file: {e}")
    print(f"\u2713 Successfully downloaded from {site}")


        
