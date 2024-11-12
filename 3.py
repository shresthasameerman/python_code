def main():
    # Prompt for the number of students and group size
    num_students = int(input("How many students? "))
    group_size = int(input("Required group size? "))
    
    # Calculate the number of groups and leftover students
    num_groups = num_students // group_size
    leftover_students = num_students % group_size
    
    # Determine the correct grammar for the output
    if leftover_students == 1:
        print(f"There will be {num_groups} groups with {leftover_students} student left over.")
    else:
        print(f"There will be {num_groups} groups with {leftover_students} students left over.")

# Run the program
if __name__ == "__main__":
    main()