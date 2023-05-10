def get_student_name(stuid : str):                                      # str, 'ap172'
    """ - expects a student id (string)
        - loops through student_db_names.txt and reads each student id
        - if the student id is found, returns the student's full name,
          built from the first name and last name in the line
        - if the student id is not found, returns None

        Argument:      a student id (string)
        Return value:  the student's full name, or None if not found
    """
    # YOUR CODE HERE
    student_db = open("student_db_names.txt")                           # 'File' object
    for line in student_db:                                             # str, 'id:fname:lname:address:city:state:zip'
        data = line.split(":")                                          # List, ['id', 'fname', 'lname', 'address', 'city', 'state', 'zip']
        if data[0] == stuid and data[0] != "id":                        # bool, False
            return f"{data[1]} {data[2]}"

sid = 'ap172'
name = get_student_name(sid)
print(name)                     # Anton Perillo

sid = 'jab44'
name = get_student_name(sid)
print(name)                     # Janine Brillo

sid = 'xxx'
name = get_student_name(sid)
print(name)                     # None