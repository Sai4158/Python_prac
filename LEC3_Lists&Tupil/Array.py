# list in py 

marks = [5.54,435.6,4.76,56.7,34.6]

print(marks)
print(type(marks))

# {34.6, 435.6, 4.76, 5.54, 56.7}
# <class 'list'>

# this will print the length
print("length is: ", len(marks))
# length is:  5

# printing the index 
print(marks[0])
print(marks[1])
print(marks[2])


# -------------

Student = ["Sai", "Aggam","Pranav"]
Student[0] = "das"
print(Student)
# ['das', 'Aggam', 'Pranav']


# Slicing in list 
stu = Student[0:2]
print(stu)
# ['das', 'Aggam']