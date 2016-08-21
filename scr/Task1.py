file = open("MoviesData.txt", "r")
allMovies = file.readlines()

for movie in allMovies:
    print(movie)

file.close()
        

















