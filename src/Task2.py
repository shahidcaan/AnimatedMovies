"""
Task 2a
Write a modified version of function readAllRecords()
to read all the records from the file and return the
records as a Python list. 
"""
def readAllRecords():
    
    file = open("MoviesData.txt", "r")
    allMovies = file.readlines()
    file.close()

    return allMovies

"""
Task 2b
Write another function displayAllNames() that uses
or calls the method in part a to get the list, iterate
through the it and display ONLY the titles (movies name) of
all the movies.
"""
def displayAllNames():

    movies = readAllRecords()

    for movie in movies:
        allFields = movie.split("%")
        #Task 2c Adding movie release year to part b part of program.
        print(allFields[1] +" - "+allFields[2])

   
# Calling the defined function to execute it
displayAllNames()

  
        
