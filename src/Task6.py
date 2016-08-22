"""
Reusing the readAllRecords() function created earlier in the tasks
"""
def readAllRecords():
    
    file = open("MoviesData.txt", "r")
    allMovies = file.readlines()
    file.close()

    return allMovies
"""
Task 6a
Write a function getYearTitles (year) that retrieve
all the movies titles specified by the parameter (year),
and return them as a list. Test the method before you
move to the next question.  
"""
def getYearTitles(year):
    allMovies = readAllRecords()
    yearTitles = []
    for movie in allMovies:
        movieFields = movie.split("%")
        if (movieFields[2] == year ):
            yearTitles.append(movieFields[1])
    return yearTitles

"""
Task 6b
Write a function sortAlphaTitles (yearTitles) that takes
one parameter titles of specific year, sort them in
alphabetical order and return the sorted list.
Test the method before you move to the next question.  
"""
def sortTitlesAZ(yearTitles):
    yearTitles.sort()
    return yearTitles

"""
Task 6c
Write a function sortRevAlphaTitles(year) that takes
one parameter titles of specific year, sort them in
reverse alphabetical order and return the sorted list.
Test the method before you move to the next question.   
"""
def sortTitlesZA(yearTitles):
    yearTitles.sort(reverse=True)
    return yearTitles    

"""
Task 6d
Write a function printSortedTitles(sortedYearTitles), that takes one
parameter sorted titles list of type List, loop through it using
the for loop and display the titles in the list. 
"""
def printSortedTitles(sortedYearTitles):
    for title in sortedYearTitles:
        print(title)
"""
Task 6e
Write a function getUserYear(), that takes no parameter and prompt
the user to enter the year of movies. The method returns the year.
"""
def getUserYear():
    year = input("Please enter the year of movies : ")
    return year
            
        
  








