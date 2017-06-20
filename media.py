import webbrowser

"""Provides a way to store movie related information"""

class Movie():
	
	#Constructor taking object calling it and 4 movie instance variables
	def __init__(self, movie_name, movie_storyline, poster_image, movie_trailer):  
		self.title = movie_name
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = movie_trailer

    #Instance Method to show trailer on browser using movie youtube url
	def show_trailer(self):  
	    webbrowser.open(self.trailer_youtube_url)	