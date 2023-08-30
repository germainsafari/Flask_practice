# list_student_heights = input("input a list of students")
# student_heights = list_student_heights.split()

# for i in range(0,  len(student_heights)):
#     student_heights[i] = int(student_heights[i])
#     print(student_heights)

student_heights = input("Input a list of student heights (comma-separated): ")
heights_list = student_heights.split(",")
for i in range(0, len(heights_list)):
    heights_list[i] = int(heights_list[i])
print(heights_list)
