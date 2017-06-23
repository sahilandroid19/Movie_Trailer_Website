import webbrowser

"""Provides a way to store movie related information"""


class Movie():

    def __init__(self, movie_name, movie_storyline,
                 poster_image, movie_trailer):
        """Constructor taking object and 4 movie instance variables"""
        self.title = movie_name
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
        """ Opens trailer in a web browser """
        webbrowser.open(self.trailer_youtube_url)
