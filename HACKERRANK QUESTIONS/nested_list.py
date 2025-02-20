if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score]);
        
    #we use set to get unique value 
    student_sorted = sorted(set([student[1] for student in students]));
    # here we get a single second lowest value 
    second_lowest = student_sorted[1];
    #return the sorted name which score is equal to the second lowest
    sorted_student_lowest = sorted([student[0] for student in students if student[1] == second_lowest])
    
    for student in sorted_student_lowest:
        print(student);