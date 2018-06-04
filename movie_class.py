# Practice for classes in Python
import webbrowser

class Movie():
    """This class provides a way to store movie related information"""
    VALID_RATINGS = ["G","PG","PG-13","R"]

    def __init__(self,movie_title,movie_storyline,poster_image,trailer_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer = trailer_url
    
    def show_trailer(self):
        webbrowser.open(self.trailer)


toy_story = Movie("Toy Story", "A story of a boy and his toys that come to life","http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=vwyZH85NQC4")
avatar = Movie("Avatar", "A marine on an alien planet","http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")
avengers = Movie("Avengers", "Heroes come together to save earth","https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg", "https://www.youtube.com/watch?v=eOrNdBpGMv8")
