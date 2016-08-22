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

"""
Task 5c
Write a function printSortedTitles(sortedTitlesList), that takes
one parameter sorted titles list of type List, loop through it
using the for loop and display the titles in the list. 
"""
def printSortedTitles(sortedTitlesList):
    for title in sortedTitlesList:
        print(title)
"""
Task 5d
Write a function chooseSorting that displays the choice menu to
the user to choose the sorting type (Part a or Part c) and execute
the appropriate function. Within the choice the program asks the user
to enter the year. The function should display the menu as follows:

Enter 1 to sort Movies Titles from A-Z
Enter 2 to sort Movies Titles from Z-A 
Enter 3 to exit the program

"""
def chooseSorting():

    userChoice = ""

    while (userChoice != "3"):

        userChoice = input("***************************************"\
                           "\nEnter 1 to sort Movies Titles from A-Z"\
                           "\nEnter 2 to sort Movies Titles from Z-A "\
                           "\nEnter 3 to exit the program"\
                           "\n*************************************"\
                           "\nEnter your choice here : ")
        sortedTitlesList = []
        if userChoice == "1":
            year = input ("Enter the movies year : ")
            sortedTitlesList = sortAlphaTitles(year)
            printSortedTitles(sortedTitlesList)

        elif userChoice == "2":
            year = input ("Enter the movies year : ")
            sortedTitlesList = sortRevAlphaTitles(year)
            printSortedTitles(sortedTitlesList)

        else:
            print("Program Terminated...")
   

chooseSorting()















