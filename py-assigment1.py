from statistics import mean

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

    print(f"\nYour marks are: {course_marks}.\n" )
    return course_marks

def calculate_grade(data):
    """
    Find the average marks and issue a grade
    """
    print("Calculating your grades...\n")

    avg = round(mean(data.values()), 2)

    print((f"The average for your {len(data)} course(s) is: {avg}."))
    
    if avg >= 90 and avg <= 100:
        print("Your grade is A+")
    elif avg >= 80 and avg <= 89:
        print("Your grade is B")
    elif avg >= 70 and avg <= 79:
        print("Your grade is C")
    elif avg >= 60 and avg <= 69:
        print("Your grade is D")
    else:
        print("Your grade is F")

def main():
    """
    Runs all the function for the program
    """
    course_data = get_course_marks()
    calculate_grade(course_data)
    print("\n")

main()
