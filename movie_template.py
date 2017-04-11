class Movie():
    """ The data structure for holding individual Movies """

    def __init__(self, name, poster_url, youtube_url):
        """ __init__ method.

            Initialises the Movie object

               Args:
                   name (str): Name of the movie.
                   poster_url (str): The URL for the BOX-ART for the movie
                   youtube_url (str): The URL for the youtube trailer or TV-SPOT for the movie.

        """
        self.title = name
        self.poster_image_url = poster_url
        self.trailer_youtube_url = youtube_url
        # print self.__init__.__doc__


    def show_full_info(self):
        """show_full_info method

               Displays the Movie name, box-art URL and the youtube URL for the movie

                Args:
                    none.

                Returns:
                   nothimg.

                """
        print (
            "The name of the movie is " + self.title + "\n The poster url is" +
            self.poster_image_url + "\n The youtube_url is " + self.trailer_youtube_url)
        # print self.show_full_info.__doc__
