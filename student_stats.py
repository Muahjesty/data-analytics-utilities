import sys
import numpy as np

def main():
    # read from roster2
    records = []
    with open("roster2.dat", "r") as f:
        for line in f:
            if line.strip():
                name, age, major, gpa = line.strip().split(",")
                records.append((name.strip(), int(age), major.strip(), float(gpa)))
                
    # define array datatype
    student_dtype = [
        ('name', 'U50'), 
        ('age', 'i4'), 
        ('major', 'U4'), 
        ('gpa', 'f8')
    ]
    
    # make NumPy array
    arr = np.array(records, dtype=student_dtype)
    
    # a. average GPA of all students
    avg_gpa_all = np.mean(arr['gpa'])
    print(f"{avg_gpa_all}")
    
    # b. max GPA of students majoring in CS
    cs_students = arr[arr['major'] == 'CS']
    max_cs_gpa = np.max(cs_students['gpa'])
    print(f"{max_cs_gpa}")
    
    # c. number of students w/ a GPA over 3.5
    high_gpa_count = np.sum(arr['gpa'] > 3.5)
    print(f"{high_gpa_count}")
    
    # d. average GPA of students who are at least 25 years old
    older_students = arr[arr['age'] >= 25]
    avg_gpa_older = np.mean(older_students['gpa'])
    print(f"{avg_gpa_older}")
    
    # e. major w/ the highest average GPA in students at most 22 years old
    young_students = arr[arr['age'] <= 22]
    unique_majors = np.unique(young_students['major'])
    
    best_major = None
    highest_avg = -1.0
    
    for major in unique_majors:
        major_gpas = young_students[young_students['major'] == major]['gpa']
        major_avg = np.mean(major_gpas)
        if major_avg > highest_avg:
            highest_avg = major_avg
            best_major = major
            
    print(f"{best_major}")

if __name__ == "__main__":
    main()