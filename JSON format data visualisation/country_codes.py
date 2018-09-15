from pygal.maps.world import COUNTRIES

def get_country_code(country_name):

	"""Retruns the function with the two digit name of the given country"""

	for code, name in COUNTRIES.items():

		if name== country_name:
			return code

			#if the country was not found return None
	return None



print(get_country_code('Nepal'))
print(get_country_code('India'))
print(get_country_code('China'))