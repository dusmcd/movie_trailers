import media
import fresh_tomatoes

# Initializing 6 instances of Movie objects w/ accompanying data

space_odyssey = media.Movie("2001: A Space Odyssey",
                            "A mission to Jupiter with the help of HAL, "
                            "the supercomputer.",
                            "https://1.bp.blogspot.com/-RpZ1rglEeIk/T7TyEH0sEeI/AAAAAAAAEcA/O5XF3t56MY8/s1600/2001+A+Space+Odyssey+%281968%29+Space+Station+One+by+Robert+McCall.jpg",    # NOQA
                            "https://www.youtube.com/watch?v=XHjIqQBsPjk")

oceans_eleven = media.Movie("Ocean's Eleven",
                            "Danny Ocean and his crew take on a "
                            "nearly-impossible casino heist.",
                            "https://www.movieposter.com/posters/archive/main/186/MPW-93256",   # NOQA
                            "https://www.youtube.com/watch?v=n3epi9hPbqQ")


titans = media.Movie("Remember the Titans",
                     "A coach leads his team to victory in a "
                     "racially-divided region.",
                     "https://images-na.ssl-images-amazon.com/images/I/510TwairLCL.jpg",   # NOQA
                     "https://www.youtube.com/watch?v=nPhu9XsRl4M")

rudy = media.Movie("Rudy",
                   "A man tries to live his dream of being a "
                   "Notre Dame football player.",
                   "http://www.impawards.com/1993/posters/rudy.jpg",
                   "https://www.youtube.com/watch?v=eEFG8QA7y2w")

bourne_identity = media.Movie("The Bourne Identity",
                              "In a case of severe memory loss, Jason Bourne "
                              "struggles to find out who he really is.",
                              "http://www.impawards.com/2002/posters/bourne_identity_xlg.jpg",   # NOQA
                              "https://www.youtube.com/watch?v=FpKaB5dvQ4g")

walter_mitty = media.Movie("The Secret Life of Walter Mitty",
                           "While on the verge of losing his job, Walter "
                           "Mitty embarks on an exciting journey.",
                           "http://www.impawards.com/2013/posters/secret_life_of_walter_mitty_ver8_xlg.jpg",   # NOQA
                           "https://www.youtube.com/watch?v=QD6cy4PBQPI")

movies = [space_odyssey, oceans_eleven, titans, rudy,
          bourne_identity, walter_mitty]

# Call the open_movies_page method from the fresh_tomatoes file
# that will create the html file that displays data in this file

fresh_tomatoes.open_movies_page(movies)
