
def readAllRecords():
    file = open("MoviesData.txt", "r")
    allMovies = file.readlines()

    for movie in allMovies:
        print(movie)

    file.close()
        

userOption = ""

while userOption != "2":
      userOption = input("Enter 1 to display records\
                         \nEnter 2 to exit the program : ")
      if userOption == "1":
          readAllRecords()
print("Program Terminated")

















