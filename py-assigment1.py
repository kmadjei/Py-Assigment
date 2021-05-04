def get_course_marks():
    """
    Get the number of courses user has completed
    """

    num_of_courses = input("Please enter the:  ")

    course_marks = {}

    for course in range(num_of_courses):
        
        while True:
            try:
                mark = float(input(f"Please enter your marks for course {course + 1}: "))
                if mark < 0:
                    raise ValueError
                else:
                    course_marks[f"Course {course + 1}"] = mark
                    break   
            except TypeError:
                print(f"Invalid data: {mark}. Please enter an actual number.\n")
            except ValueError:
                print(f"You entered: {mark}. Your marks cannot be negative. Please Try again.\n")