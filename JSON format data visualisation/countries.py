
# there is a slight change in the import , updated library
from pygal.maps.world import COUNTRIES

# print the two word coutry code

for country_code in sorted(COUNTRIES.keys()):

	print(country_code, COUNTRIES[country_code])