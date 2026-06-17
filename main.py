import datetime
import time
import math
import random
import uuid
import string

# Importing Custom Package modules
from custom_utils import file_ops
from custom_utils import math_utils

# =====================================================================
# 1. Datetime and Time Module Operations
# =====================================================================
def handle_datetime_operations():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display Current Date & Time")
        print("2. Calculate Difference Between Two Dates")
        print("3. Format Current Date using strftime")
        print("4. Simple Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            now = datetime.datetime.now()
            print(f"Current Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
        
        elif choice == '2':
            d1_str = input("Enter the first date (YYYY-MM-DD): ")
            d2_str = input("Enter the second date (YYYY-MM-DD): ")
            try:
                d1 = datetime.datetime.strptime(d1_str, "%Y-%m-%d")
                d2 = datetime.datetime.strptime(d2_str, "%Y-%m-%d")
                diff = abs((d2 - d1).days)
                print(f"Difference: {diff} days")
            except ValueError:
                print("Invalid date format! Use YYYY-MM-DD.")
                
        elif choice == '3':
            now = datetime.datetime.now()
            print("Custom formats:")
            print(f"Format 1 (DD/MM/YYYY): {now.strftime('%d/%m/%Y')}")
            print(f"Format 2 (Day, Month DD, YYYY): {now.strftime('%A, %B %d, %Y')}")
            
        elif choice == '4':
            print("Press ENTER to start the stopwatch. Press ENTER again to stop it.")
            input()
            start_time = time.time()
            print("Stopwatch started...")
            input()
            end_time = time.time()
            elapsed = end_time - start_time
            print(f"Elapsed Time: {elapsed:.2f} seconds")
            
        elif choice == '5':
            try:
                seconds = int(input("Enter countdown time in seconds: "))
                print("Starting countdown...")
                while seconds > 0:
                    print(seconds, end="... ", flush=True)
                    time.sleep(1)
                    seconds -= 1
                print("\nTime's up!")
            except ValueError:
                print("Please enter a valid integer.")
                
        elif choice == '6':
            break
        else:
            print("Invalid choice. Try again.")
        print("="*30)

# =====================================================================
# 2. Built-in Math Module Operations
# =====================================================================
def handle_math_operations():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations (Sin/Cos/Tan)")
        print("4. Area of Geometric Shapes")
        print("5. Custom Math Utilities (Unit Conversion & Advanced)")
        print("6. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                num = int(input("Enter a number: "))
                if num < 0:
                    print("Factorial is not defined for negative numbers.")
                else:
                    print(f"Factorial: {math.factorial(num)}")
            except ValueError:
                print("Invalid integer input.")
                
        elif choice == '2':
            try:
                p = float(input("Enter principal amount: "))
                r = float(input("Enter rate of interest (in %): "))
                t = float(input("Enter time (in years): "))
                # Formula: A = P * (1 + r/100)^t
                amount = p * math.pow((1 + r / 100), t)
                ci = amount - p
                print(f"Compound Interest: {ci:.2f}")
                print(f"Total Amount: {amount:.2f}")
            except ValueError:
                print("Invalid numerical input.")
                
        elif choice == '3':
            try:
                deg = float(input("Enter angle in degrees: "))
                rad = math.radians(deg)
                print(f"Sin({deg}°): {math.sin(rad):.4f}")
                print(f"Cos({deg}°): {math.cos(rad):.4f}")
                print(f"Tan({deg}°): {math.tan(rad):.4f}")
            except ValueError:
                print("Invalid input.")
                
        elif choice == '4':
            print("Choose shape: 1. Circle  2. Rectangle")
            shape = input("Choice: ")
            if shape == '1':
                r = float(input("Enter radius: "))
                print(f"Area of Circle: {math.pi * r * r:.2f}")
            elif shape == '2':
                l = float(input("Enter length: "))
                w = float(input("Enter width: "))
                print(f"Area of Rectangle: {l * w:.2f}")
                
        elif choice == '5':
            print("\n--- Advanced Custom Math Utils ---")
            print("1. Celsius to Fahrenheit")
            print("2. Kilometers to Miles")
            print("3. Volume of a Cylinder")
            sub_choice = input("Choice: ")
            if sub_choice == '1':
                c = float(input("Enter temperature in Celsius: "))
                print(f"{c}°C = {math_utils.celsius_to_fahrenheit(c):.2f}°F")
            elif sub_choice == '2':
                km = float(input("Enter distance in KM: "))
                print(f"{km} KM = {math_utils.kilometers_to_miles(km):.2f} Miles")
            elif sub_choice == '3':
                r = float(input("Enter cylinder radius: "))
                h = float(input("Enter cylinder height: "))
                print(f"Volume: {math_utils.calculate_cylinder_volume(r, h):.2f}")
                
        elif choice == '6':
            break
        else:
            print("Invalid choice.")
        print("="*30)

# =====================================================================
# 3. Random Module Operations
# =====================================================================
def handle_random_operations():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Simulate Random Dataset Sampling")
        print("6. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            low = int(input("Enter lower bound: "))
            high = int(input("Enter upper bound: "))
            print(f"Random Number: {random.randint(low, high)}")
            
        elif choice == '2':
            size = int(input("Enter list size: "))
            rand_list = [random.randint(1, 100) for _ in range(size)]
            print(f"Generated List: {rand_list}")
            
        elif choice == '3':
            length = int(input("Enter password length: "))
            # Mix of elements to generate a strong password like 'Kd8@qzP!'
            chars = string.ascii_letters + string.digits + "@#$!%&*^"
            password = "".join(random.choice(chars) for _ in range(length))
            print(f"Generated Password: {password}")
            
        elif choice == '4':
            # Typical 4 or 6-digit string OTP numeric generation
            digits = int(input("Enter OTP length (e.g., 4 or 6): "))
            otp = "".join(random.choice(string.digits) for _ in range(digits))
            print(f"Generated OTP: {otp}")
            
        elif choice == '5':
            dataset = ["User_A", "User_B", "User_C", "User_D", "User_E", "User_F"]
            print(f"Dataset: {dataset}")
            k = int(input(f"Enter sample size (max {len(dataset)}): "))
            if k <= len(dataset):
                sample = random.sample(dataset, k)
                print(f"Random Sample: {sample}")
            else:
                print("Sample size exceeds dataset size.")
                
        elif choice == '6':
            break
        else:
            print("Invalid choice.")
        print("="*30)

# =====================================================================
# 4. UUID Module Operations
# =====================================================================
def handle_uuid_operations():
    print("\nGenerate Unique Identifiers:")
    print("1. Generate standard UUID (UUID4)")
    print("2. Simulate session token assignment")
    opt = input("Choice: ")
    
    if opt == '1' or opt == '2':
        unique_id = uuid.uuid4()
        print(f"Generated UUID: {unique_id}")
    else:
        print("Returning to menu.")
    print("="*30)

# =====================================================================
# 5. File Operations Custom Module Interface
# =====================================================================
def handle_file_operations():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            filename = input("Enter file name: ")
            file_ops.create_file(filename)
        elif choice == '2':
            filename = input("Enter file name: ")
            data = input("Enter data to write: ")
            file_ops.write_to_file(filename, data)
        elif choice == '3':
            filename = input("Enter file name: ")
            file_ops.read_from_file(filename)
        elif choice == '4':
            filename = input("Enter file name: ")
            data = input("Enter data to append: ")
            file_ops.append_to_file(filename, data)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")
        print("="*30)

# =====================================================================
# 6. Dynamic Exploration Module Feature
# =====================================================================
def handle_dynamic_exploration():
    print("\nExplore Module Attributes:")
    mod_name = input("Enter module name to explore (e.g., math, datetime, random, uuid): ").strip()
    
    # Mapping strings directly to imported target objects
    modules_map = {
        "math": math,
        "datetime": datetime,
        "random": random,
        "uuid": uuid,
        "file_ops": file_ops,
        "math_utils": math_utils
    }
    
    if mod_name in modules_map:
        attributes = dir(modules_map[mod_name])
        print(f"Available Attributes in {mod_name} module:")
        # Displaying the first 10 attributes cleanly mirroring the example image formats
        print(attributes[:10], "...") 
    else:
        print(f"Module '{mod_name}' is not pre-loaded or invalid for this exploration interface.")
    print("="*30)

# =====================================================================
# Main App Controller Execution Block
# =====================================================================
def main():
    while True:
        print("===============================")
        print("Welcome to Multi-Utility Toolkit")
        print("===============================")
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        print("===============================")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            handle_datetime_operations()
        elif choice == '2':
            handle_math_operations()
        elif choice == '3':
            handle_random_operations()
        elif choice == '4':
            handle_uuid_operations()
        elif choice == '5':
            handle_file_operations()
        elif choice == '6':
            handle_dynamic_exploration()
        elif choice == '7':
            print("===============================")
            print("Thank you for using the Multi-Utility Toolkit!")
            print("===============================")
            break
        else:
            print("Invalid selection. Please choose options 1 through 7.")

if __name__ == "__main__":
    main()