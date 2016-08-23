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
Write a function getUserChoice(), that takes no parameter and prompt
the user to enter the year of movies or enter "t" if the user do not
want to proceed with the program and terminate the program
. The method returns the year.
"""
def getUserChoice():
    userChoice = ""
    # Task 6i - Please see in the worksheet
    while (userChoice != "i" and userChoice != "t"):
        userChoice = input("------------------------------------"\
                     "\nEnter i to insert the year of movies"\
                     "\nEnter t to terminate the program"\
                     "\n------------------------------------"\
                     "\nEnter your choice here : ")
    return userChoice

"""
Task 6f
Write a function getUserYear(), that takes no parameter and prompt
the user to enter the year of movies. The method returns the year.
"""
def getUserYear():
    year = "yyyy"
    while not year.isnumeric() or len(year) > 4 or len(year) < 4:
        year = input("Please enter the year of movies : ")
    return year
            
"""
Task 6g
Write a function getUserSorting(), that takes no parameter and prompt
the user to select the sorting type and return the user choice of sorting. 
"""
def getUserSorting():
    sortingType = input("--------------------------------------"\
                           "\nEnter a to sort Movies Titles from A-Z"\
                           "\nEnter z to sort Movies Titles from Z-A "\
                           "\n--------------------------------------"\
                           "\nEnter your choice here : ")
    return sortingType        

"""
Task 6h
Write a function mainFunction() with no parameter that makes the
use of all the previous functions to run the program. 
"""
def mainFunction():

    userChoice = ""
    while userChoice != "t":
        userChoice = getUserChoice()
        if userChoice == "i":
            year = getUserYear()
            yearTitles = getYearTitles(year)
            sortedList = []
            sortingType = getUserSorting()
            if sortingType == "a":
                sortedList = sortTitlesAZ(yearTitles)
            elif sortingType == "z":
                sortedList = sortTitlesZA(yearTitles)
            print("Animated movies of year "+ year +" sorted in "+ sortingType )
            printSortedTitles(sortedList)
           
        else:
            print("Program Terminated. Thank you") 


mainFunction()

