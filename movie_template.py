class Movie():
    """ The data structure for holding individual Movies """

    def __init__(self, name, poster_url, youtube_url):
        self.title = name;
        self.poster_image_url = poster_url
        self.trailer_youtube_url = youtube_url

    def show_full_info(self):
        print (
        "The name of the movie is " + self.title + "\n The poster url is" + self.poster_image_url + "\n The youtube_url is " + self.trailer_youtube_url)
