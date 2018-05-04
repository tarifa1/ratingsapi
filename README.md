# ratingsapi

This app was created as part of a code challenge to build an API that interfaces with the OMDB API (https://www.omdbapi.com/)

# Deployment to clean Linux machine 
To set up a fresh deployment of this app to a local Linux or Mac OS machine:

1) Download the repository contents or fork/clone a copy of the repository to your local machine
2) From your terminal window/command line,create a virtual environment:
    `python mkvirtualenv ratings`
3) Navigate to the directory where your virtual environment was created and activate it:
    `source ratings/bin/activate`
4) Install the requirements.txt dependencies:
    `pip install -r requirements.txt`
5) The Django project should already be in place, so to run the server for the API run the following from the ratings_api directory:
    `python manage.py runserver`

# Logging In , Using the API

1) Running the server should make the API accessible to http://127.0.0.1:8000/
2) You should be re-directed to the login page : please log in with the credentials provided via email
3) From here, the API admin page is visible. 
4) Movies can be added by clicking the "Add" button under "MOVIE_POST"
5) Clicking the "Movies" link under "MOVIE_POST" will list all the movies that have been entered; for details of those particular movies, including Title, User Rating as well as created/updated times, please go to http://127.0.0.1:8000/admin/movie_post/movies/movies where this information can be accessed in JSON format
6) To edit existing entries, navigate to http://127.0.0.1:8000/admin/movie_post/movies/ and click on a movie title to update its score.
7) Details for a single movie have not yet been added
8) Pulling in data from OMDB Api has yet to be integrated into this API ; please see the next section on how to use the stand-alone python script provided in this repository to access OMDB's data

# omdb_api_fetch.py

1) Since this API project has not completed all of it's acceptance criteria (details for a single film and OMDB data are not yet integrated), this python script is here to provide a tool that can help address both those tasks
2) To run the app, simply navigate into the directory it is located in and run the following (passing in a movie title in quotes):
    `python omdb_api_fetch.py ["Movie title"]`
3) The Python script should return the movie title, metacritic score, imdb score, as well as the imdb_id. The Python script takes the JSON data from the OMDB website and then reads it as a dictionary. The values being returned are being read from that dictionary object. 
