# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   Ryan Stoddard,03/03/2026,Created Script
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
FILE_NAME: str = "Enrollments.json"
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

# Define the program's data
menu_choice: str = ''  # Hold the choice made by the user.
students: list = []  # a table of student data

# Processing --------------------------------------- #
class FileProcessor:
    """
        A collection of processing layer functions that work with JSON files

        ChangeLog: (Who, When, What)
        Ryan Stoddard,03/03/2026,Created Class
        """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from an external JSON file

        ChangeLog: (Who, When, What)
        Ryan Stoddard,03/03/2026,Created function
        """
        file = None

        try:
            file = open(file_name, "r")
            student_data = json.load(file)
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file is not None and file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to an external JSON file

        ChangeLog: (Who, When, What)
        Ryan Stoddard,03/03/2026,Created function
        """
        file = None

        try:
            file = open(file_name, "w")
            json.dump(student_data, file, indent=2)
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file is not None and file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
       A collection of presentation layer functions that manage user input and output

       ChangeLog: (Who, When, What)
       Ryan Stoddard,03/03/2026,Created Class
       Ryan Stoddard,03/03/2026,Added a function to display custom error messages
       Ryan Stoddard,03/03/2026,Added menu output and input functions
       Ryan Stoddard,03/03/2026,Added a function to input new data
       Ryan Stoddard,03/03/2026,Added a function to display the data
       """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        Ryan Stoddard,03/03/2026,Created function
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        Ryan Stoddard,03/03/2026,Created function
        """
        print()
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        Ryan Stoddard,03/03/2026,Created function
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing the exception object to avoid the technical message
        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """ This function displays all student name and course information to the user

        ChangeLog: (Who, When, What)
        Ryan Stoddard,03/03/2026,Created function
        """

        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gathers student data from the user

        ChangeLog: (Who, When, What)
        Ryan Stoddard,03/03/2026,Created function
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")

            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)

            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data

#  End of function definitions

# Beginning of the main body of this script
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Repeat the following tasks
while True:
    IO.output_menu(menu=MENU) #Displays the menu

    menu_choice = IO.input_menu_choice() #Takes user input for menu choice

    if menu_choice == "1":  # Get new data (and display the change)
        students = IO.input_student_data(student_data=students)
        IO.output_student_courses(student_data=students)
        continue

    elif menu_choice == "2": # Displays current data
        IO.output_student_courses(student_data=students)
        continue

    elif menu_choice == "3": # Saves data to external json file
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4":  # Ends the program
        break  # out of the while loop