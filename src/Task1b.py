#Define a new function readAllRecords()
def readAllRecords():
    file = open("MoviesData.txt", "r")
    allMovies = file.readlines()
    file.close()

    for movie in allMovies:
        print(movie)

    
# Calling the defined function to execute it       
readAllRecords()















