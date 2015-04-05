import fresh_tomatoes
import media
"""Store data here in instances of classs movie. 
To create a class call movie.Movie(title, synopsis, posterURL, YouTubeURL)"""

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYiP1YRRmNotl5iHHPP-HtEUw8qtGq6YVfDLZFlMCdpvzoT8HbcG9mdg",
                        "https://youtu.be/KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "Blue alien dudes",
                     "http://www.impawards.com/2009/posters/avatar.jpg",
                     "https://youtu.be/d1_JBMrrYw8")

inglorious_basterds = media.Movie("Inglorious Basterds",
                                  "Freelance soldiers kill Nazis; languages galore",
                                  "http://upload.wikimedia.org/wikipedia/en/c/c3/Inglourious_Basterds_poster.jpg",
                                  "https://youtu.be/KnrRy6kSFF0")
ratatouille = media.Movie("Ratatouille",
                          "Rat chef in Paris; doesn't speak French",
                          "http://www.impawards.com/2007/posters/ratatouille.jpg",
                          "https://youtu.be/c3sBBRxDAqk")

life_of_brian = media.Movie("Life of Brian",
                            "Brian is mistaken for Jesus",
                            "http://www.impawards.com/1979/posters/life_of_brian_ver3.jpg",
                            "https://youtu.be/TKPmGjVFbrY")

skyfall = media.Movie("Skyfall",
                      "James Bond is angry",
                      "http://www.impawards.com/2012/posters/skyfall.jpg",
                      "https://youtu.be/6kw1UVovByw")

bourne_identity = media.Movie("The Bourne Identity",
                              "Man forgets who he is.",
                              "http://www.impawards.com/2002/posters/bourne_identity.jpg",
                              "https://youtu.be/FpKaB5dvQ4g")




movies = [toy_story, avatar, inglorious_basterds, ratatouille, life_of_brian, skyfall, bourne_identity]
fresh_tomatoes.open_movies_page(movies)

