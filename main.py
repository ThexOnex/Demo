import random
import string

# Function to generate a random string of letters and digits
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Create a random Python file
file_name = "random_script.py"
num_lines = 50  # Number of lines of code
line_length = 80  # Length of each line

# Create a random Python script
with open(file_name, "w") as file:
    for _ in range(num_lines):
        # Write a random line (mix of Python syntax and random text)
        line = f"print('{generate_random_string(line_length)}')\n"
        file.write(line)

print(f"Random Python file '{file_name}' created with {num_lines} lines.")
