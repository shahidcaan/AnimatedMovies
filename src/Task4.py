"""
Reusing the function created earlier in the tasks
"""
def readAllRecords():
    
    file = open("MoviesData.txt", "r")
    allMovies = file.readlines()
    file.close()

    return allMovies
"""
Task 4a
Write a function higestRated2012() that displays the names
of highest rated  animated movie of 2012. 
"""
def highestRated2012():
    allMovies = readAllRecords()
    higestRating = -1
    movieRecord = "";
    for movie in allMovies:
        movieFields = movie.split("%")
        if (movieFields[2] == "2012" and higestRating < float(movieFields[3])):
            higestRating = float(movieFields[3])
            movieRecord = movie
    print(movieRecord)

"""
Task 4b
Write a new function getHighestRated(year) that takes one
parameter released year and return the complete records of
the of highest rated  animated movie of that year.
"""
def getHighestRated(year):
    allMovies = readAllRecords()
    higestRating = -1
    movieRecord = "-No record found -";
    for movie in allMovies:
        movieFields = movie.split("%")
        if (movieFields[2] == year and higestRating < float(movieFields[3])):
            higestRating = float(movieFields[3])
            movieRecord = movie

    return movieRecord
    
"""
Task 4c
Write another methods displayRecord(movieRecord) that take one
parameter “movieRecords” which contain all the information about
the movie as a String. Call and get the highest rated movies
from the getHighestRated(year) and pass it to this function to
display it in the following format:

Hotel Transylvania 2 – 2015 
Ratings: 6.9/10
Duration: 89 mins
Dracula and his friends try to bring out the monster in his half human,
half vampire grandson in order to keep Mavis from leaving the hotel
"""
def displayRecord(movieRecord):

    movieFields = movieRecord.split("%")
    print(movieFields[1] +"("+movieFields[2]+") - " +movieFields[5].strip() +" mins"\
             "\nRatings : "+movieFields[3]+"/10"\
             "\nDuration : "+movieFields[5].strip()+" mins\n"\
              +movieFields[4]+".")
"""
Task 4c
Write a new function runProgram() that asks/prompts the user
to enter the year and it uses the method created in part b and
c to search & display the movie with highest ratings. 
"""
def runProgram():
    movieYear = input("Enter the year : ")
    movieRecord = getHighestRated(movieYear)
    if (movieRecord != "-No record found -"):
        displayRecord(movieRecord)
    else:
        print(movieRecord)

#Calling the defined function to execute the program
runProgram()















