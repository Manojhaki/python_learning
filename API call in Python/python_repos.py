import requests

#make an api call and store the response

import pygal
# i confused myself with lightenStyle to Light Style it took me a while to debug it
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS



url='http://api.github.com/search/repositories?q=language:python&sort=star'

r= requests.get(url)

print("status code: ",r.status_code )

# store api response in a variable

response_dict=r.json()


print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories

repo_dicts = response_dict['items']

names, plot_dicts = [], []


for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
    #because the data type hasn't been clearly defined label must be converted to string
	plot_dict={'value':repo_dict['stargazers_count'],'label':str(repo_dict['description']),'xlink': repo_dict['html_url'],}
    # above the xlink allows to create an element of the plot_dict dictonary and then pygal uses it the activate the bar clicks to their asscoiate links
	plot_dicts.append(plot_dict)

my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()

my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000


chart = pygal.Bar(my_config,style= my_style)

chart.title = 'Most-Starred Python Projects'

chart.x_labels = names

chart.add('', plot_dicts)

chart.render_to_file('python_repos.svg')

