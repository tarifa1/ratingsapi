import json
import requests
import re
import os
import sys


title_search = (sys.argv[1])
title_url = re.sub(" ","+",title_search)

url_real = "http://www.omdbapi.com/?t=%s&apikey=2da1fe75&r=json" % (title_url)

response = requests.get(url_real)

python_dictionary_values = json.loads(response.text)

return_title = python_dictionary_values['Title']
return_metascore = python_dictionary_values['Metascore']
return_imdbRating = python_dictionary_values['imdbRating']
return_id = python_dictionary_values['imdbID']

return_message = '''
Movie: %s
Metascore: %s
IMDB: %s
IMBD_id: %s
''' % (return_title,return_metascore,return_imdbRating,return_id)
 
if __name__ == "__main__":
	# print "%s should have done this a long time ago..." % (sys.argv[1])
	print return_message 