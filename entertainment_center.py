import media
import fresh_tomatoes

"""Method to instantiate movie class objects with title, 
   synopsis, poster_url, trailer_url"""


def init_movies():
    toy_story = media.Movie("Toy Story",
                            "A story of a boy and his toys that come to life"	 
                            "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # noqa 
                            "https://www.youtube.com/watch2v=vwy3H85NOG4")

    avatar = media.Movie("Avatar", 
		                 "A marine on an Alien planet", 
		                 "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # noqa 
		                 "https://www.youtube.com/watch?v=5PSNL1qE6VY")

    school_of_rock = media.Movie("School of Rock", 
		                         "Using Rock music to learn",
		                         "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",  # noqa 
		                         "https://www.youtube.com/watch2v=3PsUJFEBC74")

    ratatouille = media.Movie("Ratatouille", 
		                      "A rat is chef in paris", 
		                      "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",  # noqa 
		                      "https://www.youtube.com/watch2v=c3sBBRxDAgk")

    midnight_in_paris = media.Movie("Midnight in paris", 
		                            "Going back in time to meet authors", 
		                            "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",  # noqa 
		                            "https://www.youtube.com/watch2v=atLg2wQ12mvu")

    hunger_games = media.Movie("Hunger games", 
		                       "A really real reality show", 
		                       "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",  # noqa 
		                       "https://www.youtube.com/watch2v=PbA63a7H0bo")

    # Storing movies in a list
	movies = [toy_story, avatar, school_of_rock, ratatouille, 
             midnight_in_paris, hunger_games]
    # Passing movies to open_movies_page to show on web         
	fresh_tomatoes.open_movies_page(movies)

init_movies()	
