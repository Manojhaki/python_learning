import requests

from operator import itemgetter

url='https://hacker-news.firebaseio.com/v0/topstories.json'

r= requests.get(url)
# get the result json from the topstories to an boject submission_ids
submission_ids = r.json()

# an empty list
submission_dicts = []

# loops thorugh top 30 news from the above json
for submission_id in submission_ids[:30]:
    # creates another json url to request the information about the particular news
    url = ("https://hacker-news.firebaseio.com/v0/item/"+str(submission_id)+".json")
    submission_r = requests.get(url)

    # gets the status of the api call
    print(submission_r.status_code)
    # create an object that holds the new api call of each news
    response_dict = submission_r.json()

    # create a dictionary that holds the title , link and the number of comment from each news
    submission_dict = {
        'title': response_dict['title'],
        'link': "http://news.ycombinator.com/item?id="+str(submission_id),
        'comments': response_dict.get('descendants', 0)

    }

   # update the list of submission dicts with the dictionary submission dicts
    submission_dicts.append(submission_dict)

# sort the above dictionary based on the key number of comments
submission_dicts= sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# a seperate print statement loop to print the information about each news their title link and the number of comments
for submission_dict in submission_dicts:

    print("\nTitle:", submission_dict['title'])

    print("Discussion link:", submission_dict['link'])

    print("Comments:", submission_dict['comments'])



