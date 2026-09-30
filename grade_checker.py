def grade_batao(marks):
    if marks >= 90:
        return "A grade - Zabardast!"
    elif marks >= 75:
        return "B grade - Acha kaam!"
    elif marks >= 50:
        return "C grade - Theek hai, mehnat karo"
    else:
        return "Fail - Dobara koshish karo"

students_marks = {}

number_of_students = int(input("Kitne students ke marks check karne hain? "))

for i in range(number_of_students):
    naam = input("Student ka naam batao: ")
    marks = int(input(naam + " ke marks batao: "))
    students_marks[naam] = marks

print("\n--- Result ---")
for naam, marks in students_marks.items():
    result = grade_batao(marks)
    print(naam, "ke marks:", marks, "-", result)