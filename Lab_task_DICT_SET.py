# Defining function
def marks_dict():
    std_dict = {}
    no_of_std = int(input("Enter no of students: "))
    for i in range(no_of_std):
        std_name_key = str(input("Enter name: "))
        std_mark_value = int(input("Enter value: "))
        std_dict[std_name_key] = std_mark_value
    print(std_dict)

# Highest Mark Students:
    highest_mark = int()
    for name, mark in std_dict.items():
        if mark >= highest_mark:
            highest_mark = mark
    # Highest mark students:
    highest_students = []
    for name, mark in std_dict.items():
        if highest_mark == mark:
            highest_students.append(name)
    # For printing the name:
    for name, mark in std_dict.items():
        if highest_mark == mark:
            high_name = name
    print("Highest marks:")
    print(",".join(highest_students),f"({highest_mark})")

# Lowest Marks Students:
    lowest_mark = int()
    for name,mark in std_dict.items():
        if mark <  highest_mark:
            highest_mark = mark
            lowest_mark = mark

    # Lowest students marks:
    lowest_students = []
    for name, mark in std_dict.items():
        if lowest_mark == mark:
            lowest_students.append(name)

    # For printing the low name: 
    for name,mark in std_dict.items():
        if lowest_mark == mark:
            low_name = name
    print("Lowest marks:")
    print(",".join(lowest_students),f"({lowest_mark})")
        

# Calling function
marks_dict()