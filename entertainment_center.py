from media import Movie 
import fresh_tomatoes
#import movie class to store movies and fresh_tomatoes to render web page

#store movies to display 
shawshank = Movie("Shawshank Redemption", "A man falsely put in prison",
                      "http://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                      "https://www.youtube.com/watch?v=6hB3S9bIaco")

up = Movie("Up", "An lonely old man and a neglected kid form a friendship",
                 "http://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
                 "https://www.youtube.com/watch?v=pkqzFUhGPJg")

edge_tomorrow = Movie("Edge of Tomorrow", "A soldier repeats a day over and over until he defeats the invading aliens",
                           "http://upload.wikimedia.org/wikipedia/en/f/f9/Edge_of_Tomorrow_Poster.jpg",
                           "https://www.youtube.com/watch?v=vw61gCe2oqI")

rush = Movie("Rush", "Two rivals battle it out on the race track",
                   "http://www.impawards.com/2013/posters/rush_ver2_xlg.jpg",
                   "https://www.youtube.com/watch?v=aphGbb07xk8")

jack = Movie("Jack Reacher", "An everyday superhero",
                   "http://upload.wikimedia.org/wikipedia/en/d/d1/Jack_Reacher_poster.jpg",
                   "https://www.youtube.com/watch?v=kK7y8Ou0VvM")

book_of_eli = Movie("Book of Eli", "A lone man protects one of the last remnants of preapocolyptic society",
                        "http://upload.wikimedia.org/wikipedia/en/e/e3/Book_of_eli_poster.jpg",
                        "https://www.youtube.com/watch?v=zSMHmtaoXtI")
#collect movies to be displayed
movies=[up, rush, shawshank,edge_tomorrow,jack, book_of_eli]
#send them off to be generated into a webpage
fresh_tomatoes.open_movies_page(movies)
