import requests

#make an api call and store the response

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS 

url='http://api.github.com/search/repositories?q=language:python&sort=star'

r= requests.get(url)

print("status code: ",r.status_code )

# store api response in a variable

response_dict=r.json()


print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories

repo_dicts= response_dict['items']

names, stars=[],[]


for repo_dict in repo_dicts:
	name.append(repo_dicts['name'])
	stars.append(repo_dicts['stargazers_count'])



my_style = LS('#333366', base_style=LCS)


chart= pygal.Bar(style= my_Style,x_label_rotations=45, show_legent=False)

chart.title= 'Most-Starred Python Prohjects'

chart.x_labels= names

chart.add('', stars)

chart.render_to_file('python_repovs.svg')

