#Task 2
"""
Load data
Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ . 
As a result, store all comments in chronological order in JSON and dump it to a file.
"""

import requests
import json

url_all_com = "https://hacker-news.firebaseio.com/v0/topstories.json"
rq = requests.get(url_all_com)
print(f"Status code: {rq.status_code}")

submission_ids = rq.json()
all_comments = []

for submission_id in submission_ids[:30]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}") 

    if r.status_code == 200:
        comment_data = r.json()
        all_comments.append(comment_data)

readable_f = 'all_comments.json'
with open(readable_f, 'w') as file:
    json.dump(all_comments, file, indent=4)  

print(all_comments)


print("*"*50)


url_2 = "https://hacker-news.firebaseio.com/v0/item/39537448.json"
r = requests.get(url_2)
print(f"Status code: {r.status_code}")

response_dict = r.json()
readable_file = 'data.json'
with open (readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)

print(response_dict)



