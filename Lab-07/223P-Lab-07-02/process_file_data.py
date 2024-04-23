import os

def process_file_data():
    # Change to the directory where this script is located
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Initialize the sum
    total_sum = 0
    
    # Read data from the input file
    with open("input_data.txt", 'r') as file:
        for line in file:
            # Split the line into parts
            parts = line.split()
            for part in parts:

                if part.isdigit():
                   
                    total_sum += int(part)
                else:
                    print(f"Skipping invalid part: {part}")

    with open("output_result.txt", 'w') as file:
        file.write(str(total_sum))


process_file_data()
