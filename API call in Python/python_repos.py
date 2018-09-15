import requests

#make an api call and store the response


url='http://api.github.com/search/repositories?q=language:python&sort=star'

r= requests.get(url)

print("status code: ",r.status_code )

# store api response in a variable

response_dict=r.json()


print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories

repo_dicts= response_dict['items']

print("Repositories Returned :",len(repo_dicts))

#examine first result

repo_dict = repo_dicts[0]


print("\n Selected information about the first repository")

print('Name:',repo_dict['name'])

print('owner:', repo_dict['owner']['login'])

print('stars:', repo_dict['stargazers_count'])

print('repository:', repo_dict['html_url'])

print('created:', repo_dict['created_at'])

print('updated', repo_dict['updated_at'])


print('Description:', repo_dict['description'])



