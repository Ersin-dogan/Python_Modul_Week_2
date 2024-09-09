# Define the student records as a dictionary
students = {
    'Ahmet': {'Ara': 85, 'Final': 90, 'Oral': 80},
    'Mehmet': {'Ara': 78, 'Final': 82, 'Oral': 74},
    'Hasan': {'Ara': 90, 'Final': 92, 'Oral': 88},
    'Hüseyin': {'Ara': 65, 'Final': 70, 'Oral': 60},
    'Ali': {'Ara': 58, 'Final': 65, 'Oral': 70},
    'Veli': {'Ara': 82, 'Final': 80, 'Oral': 85},
    'Ayşe': {'Ara': 95, 'Final': 100, 'Oral': 90},
    'Fatma': {'Ara': 72, 'Final': 75, 'Oral': 78},
    'Emel': {'Ara': 69, 'Final': 73, 'Oral': 65},
    'Şükriye': {'Ara': 88, 'Final': 84, 'Oral': 80}
}

# Function to calculate GPA
def calculate_gpa(midterm, final, oral):
    return (midterm * 0.4) + (final * 0.4) + (oral * 0.2)

# Calculate each student's GPA and add it to the dictionary
for student, grades in students.items():
    gpa = calculate_gpa(grades['Midterm'], grades['Final'], grades['Oral'])
    students[student]['GPA'] = round(gpa, 2)

# Find the student with the highest GPA
highest_gpa = max(students.items(), key=lambda x: x[1]['GPA'])
print(f"The student with the highest GPA is {highest_gpa[0]} with a GPA of {highest_gpa[1]['GPA']}")

# Separate each student's name from their surname and store them in a tuple, then add to a list
name_tuples = []
for name in students.keys():
    first_name, last_name = name.split()
    name_tuples.append((first_name, last_name))

# Sort the names in alphabetical order and print the sorted list
sorted_names = sorted(name_tuples, key=lambda x: x[0])
print("Sorted names:", sorted_names)

# Keep students with a GPA below 70 in a set
low_gpa_students = set()
for student, info in students.items():
    if info['GPA'] < 70:
        low_gpa_students.add(student)

print("Students with GPA below 70:", low_gpa_students)

