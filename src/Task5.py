"""
Reusing the readAllRecords() function created earlier in the tasks
"""
def readAllRecords():
    
    file = open("MoviesData.txt", "r")
    allMovies = file.readlines()
    file.close()

    return allMovies
"""
Task 5a
Write a function sortAlphaTitles(year) that retrieve all the
movies specified by the parameter (year), sort them alphabetically
with their titles and display them with all details. Test the method
before you move to the next task.  
"""
def sortAlphaTitles(year):
    allMovies = readAllRecords()
    yearTitles = []
    for movie in allMovies:
        movieFields = movie.split("%")
        if (movieFields[2] == year ):
            yearTitles.append(movieFields[1])
    yearTitles.sort()
    return yearTitles
"""
Task 5b
Write a function sortRevAlphaTitles(year) that retrieve all
the movies specified by the parameter (year), sort them in
reverse alphabetical order with their titles and display them.
Test the method before you move to the next task.    
"""
def sortRevAlphaTitles(year):
    allMovies = readAllRecords()
    yearTitles = []
    for movie in allMovies:
        movieFields = movie.split("%")
        if (movieFields[2] == year ):
            yearTitles.append(movieFields[1])
    yearTitles.sort(reverse=True)
    return yearTitles

def printSortedTitles(year):
    sortedTitlesList = sortRevAlphaTitles(year)
    for title in sortedTitlesList:
        print(title)

printSortedTitles("2015")




