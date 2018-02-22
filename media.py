# import the class Title from title file
from title import Title


# creat an inheritance class to contain the rest of information
class Movie(Title):
    # define the function init
    def __init__(self, json_movie):
        Title.__init__(self, json_movie['title'])
        self.poster_image_url = json_movie['poster_image']
        self.trailer_youtube_url = json_movie['youtube_trailer']
