while True:
  exam_exercise = input("Exam points and exercises completed: ")
  if exam_exercise == '':
    print("all done!")
    break

points = exam_exercise.split(" ")
exam_points = int(float(points[0]))
exercise_percentage = int(float(points[1]))
exercise_points = exercise_percentage // 10
  
grade = ''

total_points = exam_points + exercise_points
print(total_points)
if total_points < 15 or exam_points < 10:
  grade = 0
elif 15 <= total_points <= 17:
  grade = 1
elif 18 <= total_points <= 20:
  grade = 2
elif 21 <= total_points <= 23:
  grade = 3
elif 24 <= total_points <= 27:
  grade = 4
elif 28 <= total_points <= 30:
  grade = 5

print(grade) 
#def statistics:
  
      
      
      # In this exercise you will write a program for printing out 
# grade statistics for a university course.

# The program asks the user for results from different students 
# on the course. These include exam points and numbers of exercises 
# completed. The program then prints out statistics based on 
# the results.

# Exam points are integers between 0 and 20. The number of exercises 
# completed is an integer between 0 and 100.

# The program kees asking for input until the user types in an empty 
# line. You may assume all lines contain valid input, which means 
# that there are two integers on each line, or the line is empty.

# And example of how the data is typed in:

# Sample output
# Exam points and exercises completed: 15 87
# Exam points and exercises completed: 10 55
# Exam points and exercises completed: 11 40
# Exam points and exercises completed: 4 17
# Exam points and exercises completed:
# Statistics:

# When the user types in an empty line, the program prints out 
# statistics. They are formulated as follows:

# The exercises completed are converted into exercise points, 
# so that completing at least 10% of the exercises grants one 
# point, 20% grants two points, and so forth. Completing all 
# 100 exercises grants 10 exercise points. The number of exercise 
# points granted is an integer value, rounded down.

# The grade for the course is determined based on the following table:

# exam points + exercise points	grade
# 0–14	0 (i.e. fail)
# 15–17	1
# 18–20	2
# 21–23	3
# 24–27	4
# 28–30	5
# There is also an exam cutoff threshold. If a student received less 
# than 10 points from the exam, they automatically fail the course, 
# regardless of their total number of points.

# With the example input from above the program would print out the 
# following statistics:

# Sample output
# Statistics:
# Points average: 14.5
# Pass percentage: 75.0
# Grade distribution:
#   5:
#   4:
#   3: *
#   2:
#   1: **
#   0: *
# Floating point numbers should be printed out with one decimal precision.

# NB: this exercise doesn't ask you to write any specific functions, 
# so you should not place any code within an if __name__ == "__main__" block. 
# If any functionality in your program is e.g. in the main function, you should 
# include the code calling this function normally, and not contain it in an if 
# block like in the exercises which specify certain functions.

# Hint:

# The user input in this program consists of lines with two integer values:

# Sample output
# Exam points and exercises completed: 15 87

# You have to first split the input line in two and then convert the sections 
# into integers with the int function. Splitting the input can be achieved in 
# the same way as in the exercise First, second and last words, but there is a 
# simpler way as well. The string method split will chop the input up nicely. 
# You will find more information by searching for python string split online.