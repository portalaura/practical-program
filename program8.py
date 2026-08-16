def copy_lines():
    n = int(input("Enter the number of lines: "))
    lines_list = []
    for i in range(n):
        line = input("\nEnter a line: ")
        lines_list.append(line)

    f = open("stories.txt", "w")
    for line in lines_list:
        f.write(line + "\n")
    f.close()

    fin = open("stories.txt", "r")
    fout = open("lines.txt", "w")

    for line in fin:
        if line[0].upper() not in ['A', 'E', 'I', 'O', 'U']:
            fout.write(line)

    fin.close()
    fout.close()

    print("contents of lines.txt:\n")
    f = open("lines.txt", "r")
    print(f.read())
    f.close()

copy_lines()