"""
Task 3a
Reusing the function created earlier in the tasks
"""
def readAllRecords():
    
    file = open("MoviesData.txt", "r")
    allMovies = file.readlines()
    file.close()

    return allMovies

"""
Task 3a
Write a method display2015Movies() that display the
animated movies released in ONLY 2015 with all the
details in the following format:

Movie name (Released Year)  | Running Time in minutes
Ratings : -/10
Description here
"""
def display2015Movies():
    allMovies = readAllRecords()

    for movie in allMovies:
        movieFields = movie.split("%")
        if (movieFields[2] == "2015"):
            print(movieFields[1] +"("+movieFields[2]+") | " +movieFields[5].strip() +" mins"\
             "\nRatings : "+movieFields[3]+"/10\n"+movieFields[4]+"\n\n")

#Calling the defined function to execute it
display2015Movies()



