
# Function Definition with Paramaters

def grade_point_average_and_cost(CourseNames,FinalGrades,CourseHours,RequiredByMajor,Cost):   

# Variables set to 0 to start
    GradeHourTotal = 0
    HourTotal = 0
    CostTotal = 0
    NumCourses = 0

# For loop to print out every entry as well as setting variables for later print statements
    for i in range(len(CourseNames)):
       print(CourseNames[i], FinalGrades[i], CourseHours[i], RequiredByMajor[i], Cost[i])
       GradeHourTotal = GradeHourTotal + (FinalGrades[i]*CourseHours[i])
       HourTotal = HourTotal + CourseHours[i]
       CostTotal = CostTotal + Cost[i]
       NumCourses = NumCourses + 1
       GradePointAverage = GradeHourTotal/HourTotal
       AverageCost = CostTotal/NumCourses

# print out GPA and Average Cost through variables set in previous For loop
    print("Grade Point Average: ", GradePointAverage)
    print("Average Cost: ", AverageCost)

# Set variables to 0 again for Major only portion
    GradeHourTotal = 0
    HourTotal = 0
    NumCourses = 0
    CostTotal = 0

# For loop again but with if statement to only print out Major Only classes
    for i in range(len(CourseNames)):
        if RequiredByMajor[i] == "yes":
           print(CourseNames[i], FinalGrades[i], CourseHours[i], RequiredByMajor[i], Cost[i])
           GradeHourTotal = GradeHourTotal + (FinalGrades[i]*CourseHours[i])
           HourTotal = HourTotal + CourseHours[i]
           CostTotal = CostTotal + Cost[i]
           NumCourses = NumCourses + 1
           GradePointAverage = GradeHourTotal/HourTotal
           AverageCost = CostTotal/NumCourses

# Print out GPA and Average Cost if there are RequiredByMajor Classes
    if HourTotal > 0:
        print("Grade Point Average: ", GradePointAverage)
        print("Average Cost: ", AverageCost)
    else:
        print("No courses in major")
        
    

CourseNames = []

FinalGrades = []

CourseHours = []

RequiredByMajor = []

Cost = []

#Here are the courses I've taken

# COURSE 1 or 0th entry in list

CourseNames.append("Physics")

FinalGrades.append(3.0)

CourseHours.append(3)

RequiredByMajor.append("no")

Cost.append(600.0)

# COURSE 2 or 1st entry in list

CourseNames.append("History")

FinalGrades.append(4.0)

CourseHours.append(5)

RequiredByMajor.append("no")

Cost.append(800.0)

# COURSE 3

CourseNames.append("Trig")

FinalGrades.append(3.75)

CourseHours.append(3)

RequiredByMajor.append("yes")

Cost.append(600.0)

# COURSE 4

CourseNames.append("English Lit")

FinalGrades.append(4.0)

CourseHours.append(4)

RequiredByMajor.append("no")

Cost.append(800.0)

# COURSE 5

CourseNames.append("Business Principles")

FinalGrades.append(4.0)

CourseHours.append(1)

RequiredByMajor.append("yes")

Cost.append(800.0)

#this accounts for all of my first and only semester at FSU so far

grade_point_average_and_cost (CourseNames, FinalGrades, CourseHours, RequiredByMajor, Cost)

print("and that is it so far ")
