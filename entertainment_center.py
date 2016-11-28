'''
Stage 3 - Make Your Own Movie Website
Module - Entertainment Center (drive Media module)
'''
import fresh_tomatoes
import media

Frozen = media.Movie("Frozen",
                     "A fearless princess who sets off on an epic journey",
                     "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",
                     "https://www.youtube.com/watch?v=FLzfXQSPBOg")

Spirited_Away = media.Movie ("Spirited Away",
                             "A young girl accidentally entered a spiritual world while moving to a new neighborhood",
                             "https://upload.wikimedia.org/wikipedia/en/3/30/Spirited_Away_poster.JPG",
                             "https://www.youtube.com/watch?v=ByXuk9QqQkk")

My_Neighbor_Totoro = media.Movie ("My Neighbor Totoro",
                                   "Two young daughters of a professor and their interactions with friendly wood spirits in postwar rural Japan",
                                   "https://upload.wikimedia.org/wikipedia/en/0/02/My_Neighbor_Totoro_-_Tonari_no_Totoro_%28Movie_Poster%29.jpg",
                                   "https://www.youtube.com/watch?v=92a7Hj0ijLs")

You_Again = media.Movie ("You Again",
                          "When a young women realizes her brother is about to marry the girl who bullied her in high school",
                          "https://upload.wikimedia.org/wikipedia/en/b/b4/You_Again_film_poster.jpg",
                          "https://www.youtube.com/watch?v=S1-UMzt9e34")

Wild_Child = media.Movie ("Wild Child",
                           "A rebellious Malibu pricess is shipped off to a strict English boarding school by her father",
                           "https://upload.wikimedia.org/wikipedia/en/f/fa/Wild_child_poster.jpg",
                           "https://www.youtube.com/watch?v=0nRzHI_zRHE")

Mean_Girls = media.Movie ("Mean Girls",
                          "High school social cliques and the damaging effects they can have on girls",
                          "https://upload.wikimedia.org/wikipedia/en/8/8f/Mean_Girls_movie.jpg",
                          "https://www.youtube.com/watch?v=KAOmTMCtGkI")

movies = [Frozen, Spirited_Away, My_Neighbor_Totoro, You_Again, Wild_Child, Mean_Girls]
fresh_tomatoes.open_movies_page (movies)
