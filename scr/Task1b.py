
def readAllRecords():
    file = open("MoviesData.txt", "r")
    allMovies = file.readlines()
    file.close()

    for movie in allMovies:
        print(movie)

    
        
readAllRecords()















