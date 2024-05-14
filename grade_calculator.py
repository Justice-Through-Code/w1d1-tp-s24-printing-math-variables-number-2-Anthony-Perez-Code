def calculate_average_grade():
    # Prompt the user for their name and store it in the student_name variable
    student_name = input("Please input your name: ")

    # Prompt the user for their scores in Math, Science, and English
    # Store the scores in the respective variables: math_score, science_score, english_score
    math_score = float(input("Please input your math score: "))
    science_score = float(input("Please input your science score: "))
    english_score = float(input("Please input your english score: "))

    # Calculate the average grade
    average_grade = (math_score + science_score + english_score)/3

    # Return the student's name and their average grade
    return student_name, average_grade

if __name__ == '__main__':
    # Call the calculate_average_grade function
    student_name, average_grade = calculate_average_grade()

    # Print the student's name and their average grade
    print(f"Your name is {student_name}, and your average score is {average_grade}.")