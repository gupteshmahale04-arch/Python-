# 1. Create one main dictionary to hold all students
all_students = {}

# 2. Use a loop to ask for 10 students
# (I will change it to 3 for this example to keep it short)
num_students = 3 

for i in range(num_students):
    print(f"\n--- Entering Information for Student {i+1} ---")
    
    # Get the roll number, which we will use as the "key"
    roll_no = input("Enter the Roll No of student: ")
    
    # Get the rest of the info
    name = input("Enter the name of student: ")
    father = input("Enter the name of father: ")
    mother = input("Enter the name of mother: ")
    father_add = input("Enter the Address of father: ")
    student_add = input("Enter the Address of student: ")
    marks = input("Enter the mark: ")

    # 3. Store this student's info in its OWN dictionary
    student_data = {
        "Name": name,
        "Father": father,
        "Mother": mother,
        "Father Address": father_add,
        "Student Address": student_add,
        "Marks": marks
    }
    
    # 4. Add this student's dictionary to the main dictionary
    #    using their roll number as the key.
    all_students[roll_no] = student_data

print("\n--- All Student Data Saved! ---")
print(all_students)


# --- Now you can "click" (look up) any student ---
print("\n--- Student Lookup ---")
roll_to_find = input("Enter a Roll No to find their information: ")

if roll_to_find in all_students:
    print(f"Data for Roll No {roll_to_find}:")
    print(all_students[roll_to_find])
else:
    print(f"Sorry, no student found with Roll No {roll_to_find}.")