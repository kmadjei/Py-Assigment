def get_course_marks():
    """
    Get the details of the courses the user has completed and validate the data.
    """

    while True:
        try:
            num_of_courses = int(input("Please enter the number of courses you are taking:  "))
            if num_of_courses < 0 :
                raise TypeError(f"{num_of_courses} cannot be below 0")
            else:
                break   
        except TypeError as e:
            print(f"Invalid data: {e}. Please enter an actual number.\n")
        except ValueError:
            print(f"Invalid entry: {num_of_courses}. Please provide an integer number.\n")

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

    print("Your marks are:", course_marks)

get_course_marks()