import os

def create_file(filename):
    try:
        with open(filename, 'w') as f:
            pass
        print("File created successfully!")
    except Exception as e:
        print(f"Error creating file: {e}")

def write_to_file(filename, data):
    try:
        with open(filename, 'w') as f:
            f.write(data)
        print("Data written successfully!")
    except Exception as e:
        print(f"Error writing to file: {e}")

def read_from_file(filename):
    if not os.path.exists(filename):
        print("Error: File does not exist.")
        return
    try:
        with open(filename, 'r') as f:
            content = f.read()
        print("File Content:")
        print(content)
    except Exception as e:
        print(f"Error reading file: {e}")

def append_to_file(filename, data):
    try:
        with open(filename, 'a') as f:
            f.write(data)
        print("Data appended successfully!")
    except Exception as e:
        print(f"Error appending to file: {e}")