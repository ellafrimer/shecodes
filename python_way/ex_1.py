"""make one line of code that takes the two lists
and makes a list of 'movie is played by actress' """


movie = ["The notebook", "Malificent", "Batman vs Superman"]
actres = ["Rachel Mcadems", "Angelina Julie", "Gal Gadot"]

# ex_1

print([movie[i] + " is played by " + s for (i, s) in enumerate(actres)])

# ex_2

movies = dict(zip(movie, actres))

# ex_3

print([k + " is played by " + v for (k, v) in movies.items()])



