import pickle

def create_file()
    f = open("student.dat", "wb")
    
    n = int(input("Enter number of students: "))
    
    for i in range(n):
        rollno = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        
        mark1 = float(input("Enter Mark 1: "))
        mark2 = float(input("Enter Mark 2: "))
        mark3 = float(input("Enter Mark 3: "))
        
        student = [rollno, name, mark1, mark2, mark3]
        pickle.dum0(student, f)
    f.close()
    print("Records stored successfully")
    
def display_file():
    f = open("student.dat", "rb")
    print("\nStudent Record: ")
    try:
        while True:
            student = pickle.load(f)
            total = student[2] + student[3] + student[4]
            avg = total/3
            print("Roll No: ", student[0])
            print("Name", student[1])
            print("Marks:", student[2], student[3], student[4])
            print("Total: ", total)
            print("Average: ", avg)
            print()
    except EOFError:
        f.close()
        
create_file()
display_file()