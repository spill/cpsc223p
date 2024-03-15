def student_info(name, age, grade, address, phone):
    # apply str.format() method for name, age and grades
    student_info = "Name: {}, Age: {}, Grade: {}".format(name, age, grade)
    print(student_info)
    
    
    
    
    formatted_address = "Address: " + address[:10] + "..."
    print(formatted_address)
    
    padded_phone = "Phone: " + phone.rjust(20, '*')
    print(padded_phone)
    
    
student_info('Ryan Trinh', 20, 'Sophmore', '8565 Connelly Mills', '2203570732')    