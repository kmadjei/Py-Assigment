from statistics import mean

def get_course_marks():
    """
    Get the details of the courses the user has completed and validate the data.
    """

    print("\nHow many courses did you complete?")
    # loop to validate user data
    while True:
        try:
            num_of_courses = input("Please enter the number of completed courses :  ")
            courses = int(num_of_courses)
            if courses < 0 :
                raise TypeError(f"{num_of_courses} cannot be below 0")
            else:
                #break loop
                break   
        except TypeError as e:
            print(f"Invalid data: {e}. Please provide a positive number.\n")
        except ValueError:
            print(f"Invalid entry: {num_of_courses}. Please enter an integer number.\n")

    # empty object/dictionary for course marks
    course_marks = {}

    #loop to get the grades
    for course in range(courses):
        
        #Loop to validate data
        while True:
            try:
                mark = input(f"Please enter your marks for course {course + 1}: ")
                # converts marks to float and validate data
                newMark = float(mark)
                if newMark < 0:
                    raise TypeError
                else:
                    # appends mark to the object
                    course_marks[f"Course {course + 1}"] = newMark
                    break   
            except TypeError:
                print(f"You entered: {mark}. Your marks cannot be negative. Please Try again.\n")
            except ValueError:
                print(f"Invalid data: {mark}. Please enter an actual number.\n")

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
