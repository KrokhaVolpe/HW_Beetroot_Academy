#Task 3
"""
Requests using multithreading
Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ . 
As a result, store all comments in chronological order in JSON and dump it to a file. For this task use Threads for making requests to reddit API.
"""

from operator import itemgetter
import requests
import json
import threading

def fetch_submission(submission_id, submission_dicts):
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)

    response_dict = r.json()

    submission_dict = {
         'title': response_dict['title'],
         'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
         'comments': response_dict.get('descendants', 0),  
     }
    submission_dicts.append(submission_dict)

def fetch_submissions(submission_ids, submission_dicts):
    threads = []
    for submission_id in submission_ids[:30]:  
        thread = threading.Thread(target=fetch_submission, args=(submission_id, submission_dicts))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def get_top_submission_dicts():
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    r = requests.get(url)
    print(f"Status code: {r.status_code}")

    submission_ids = r.json()
    submission_dicts = []
    fetch_submissions(submission_ids, submission_dicts)
    return submission_dicts

def save_comments_to_json(story_id, comments):
    with open(f'comments_for_story_{story_id}.json', 'w') as f:
        json.dump(comments, f, indent=4)
        

def get_comments_for_story(story_id):
    url = f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json'
    response = requests.get(url)
    data = response.json()
    comments = []
    if 'kids' in data:
        for comment_id in data['kids']:
            comment_url = f'https://hacker-news.firebaseio.com/v0/item/{comment_id}.json'
            comment_response = requests.get(comment_url)
            comment_data = comment_response.json()
            comments.append(comment_data)
    return comments[:20]  


def main():
    submission_dicts = get_top_submission_dicts()
    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

    for submission_dict in submission_dicts:
        print(f"\nTitle: {submission_dict['title']}")
        print(f"Discussion link: {submission_dict['hn_link']}")
        print(f"Comments: {submission_dict['comments']}")

    story_id = input("Enter the story ID: ")
    comments = get_comments_for_story(story_id)
    save_comments_to_json(story_id, comments)

if __name__ == "__main__":
    main()
