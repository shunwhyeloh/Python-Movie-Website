'''
Stage 3 - Make Your Own Movie Website
Module - Media (Use to store related information of chosen movies)
'''

#The followings are the information of chosen movies
class Movie ():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube): 
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer (self):
        webbrowser.open(self.trailer_youtube_url)
