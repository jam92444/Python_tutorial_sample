student = {}

n = int(input("Total number of  student: "))


for _ in range(n):
    
    #Get the name and list of mark on runtime 
    name, *mark = input("Enter the name and marks with space: ").split();

    #convert the marks into float value one by one using the map method.
    scores = list(map(float,mark));

    # store the key pair values in student dictionary
    student[name] = scores

# Getting the query name 
query_name = input('Enter student name to see the average marks: ');

# Calculating the average mark of the student 
student_average = sum(student[query_name]) / (len(student[query_name]))

# Showing the result
print(f"Average of {query_name} is {student_average:.2f}")