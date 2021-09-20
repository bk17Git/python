students = {
    "Harry" :  1,
    "Bastav" : 2,
    "John" : 3,
    "Marrie" : 4,
    "Katrina" : 5,
    "Chris" : 6,
    "Bossie" : 7,
    "Charlie" : 8
}

name_of_student = input("Enter the name of the student: ")

if name_of_student in students:
    print(f"{name_of_student}'s Roll no. is {students[name_of_student]}")
else:
    print(f"{name_of_student} is not there!")