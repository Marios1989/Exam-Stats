grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
print("Grades:", grades)

# Print those grades
def print_grades(grades):
    for gd in grades:
        print(gd)

print_grades(grades)

# The sum of scores
def grades_sum(scores):
  total = 0
  for score in scores:
    total += score
  return total

print(grades_sum(grades))

# Computing The Average
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

print(grades_average(grades))

# Variance
def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    return variance / len(scores)

print(grades_variance(grades))

# Standard Deviation
def grades_std_deviation(variance):
  return variance ** 0.5
  variance += grades_variance(grades)
  print(grades_std_deviation(variance))

# Review
for grade in grades:
  print(grade)
print(grades_sum(grades))
print(grades_average(grades))
print(grades_variance(grades))
print(grades_std_deviation(variance))
