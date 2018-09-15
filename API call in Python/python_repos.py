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

print("/nKeys:", len(repo_dict))



#process result

for key in sorted(repo_dict.keys()):

	print(key)