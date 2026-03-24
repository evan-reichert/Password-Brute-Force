# PROJECT OBJECTIVES
    # 1. Utilize modules such as secrets to generate a secure password for the user
    # 2. Ask the user how long they want the password to be. If it is less than 8 characters, create a demo brute force on it
    # 3. If more than 8 characters, calculate how long a potential brute force may take on it
        # (Try to make sure password contains a mix of uppercase, lowercase, numbers, and special characters. If it doesn't, the criteria is false)
    # 4. Add an entropy calculator to show the mathematical strength of the password
    # 5. Based on the entropy, display a message to the user and let them know if the password is strong enough to be used
    # 6. Print all of the qualities of the password to the user, and give them the option to generate a new one if they are not satisfied with it

import secrets
import math
import string
import itertools
import time
from tqdm import tqdm

# Alphabet definition for password generation
ALPHABET = string.ascii_letters + string.digits + "!@#$%^&*()"

print("=============================================================================================================")
print("                                             PASSWORD GENERATOR                                              ")
print("=============================================================================================================")

print("In order for a password to be considered strong, it must meet the following criteria:\n")
print("\t1. Be at least 8 characters long")
print("\t2. Contain a mix of uppercase and lowercase letters")
print("\t3. Include numbers")
print("\t4. Include special characters (e.g., !, @, #, etc.)\n")
print("The strength of the password will be evaluated based on its entropy")
print("this is a measure of how unpredictable the password is")
print("=============================================================================================================")
print("FURTHERMORE, if the password is less than 8 characters long, we will demonstrate a brute force attack on it")
print("This will show how quickly it can be cracked")
print("=============================================================================================================")


# ==================================================================================================================================
    # 1. Generate a secure password for the user using secrets module

def generate_password(length):
    password = ''.join(secrets.choice(ALPHABET) for i in range(length))
    return password

# ==================================================================================================================================
    # 2. Ask the user how long they want the password to be. If it is less than 8 characters, create a demo brute force on it
        # Utilize tqdm and time to show the progress of the brute force attack

length = int(input("Enter the desired password length (minimum 8 characters): "))
if length < 8:
    print("Password is too short. Demonstrating brute force attack...")
    print("This may take a while for longer passwords, so please be patient.")
    print("=============================================================================================================")

def conversion(seconds):
    # Years
    years = seconds // (365 * 24 * 3600)
    seconds %= (365 * 24 * 3600)
    # Days
    days = seconds // (24 * 3600)
    seconds %= (24 * 3600)
    # Hours
    hours = seconds // 3600
    seconds %= 3600
    # Minutes and Seconds
    minutes = seconds // 60
    s_seconds = int(seconds % 60)
    return f"{int(years)}y {int(days)}d {int(hours)}h {int(minutes)}m {s_seconds}s"

# Brute force demonstration
def brute_force_demo(length):  
    if length > 8:
        return "Brute force demonstration is only applicable for passwords less than 8 characters."
    else:
        target_password = generate_password(length)
        found = False
        attempts = 0
        start_time = time.time()
    
        for password_tuple in tqdm(itertools.product(ALPHABET, repeat=length), desc="Brute Forcing"):
            attempts += 1
            if ''.join(password_tuple) == target_password:
                found = True
                break
    
        end_time = time.time()
        elapsed_time = end_time - start_time
    
        if found:
            print(f"Password found after {attempts} attempts in {elapsed_time:.2f} seconds!")
        else:
            print("Password not found within the search space.")

        print("=============================================================================================================")
        return conversion(elapsed_time)
    
def brute_force_estimate(length):
    charset_size = len(ALPHABET)
    total_combinations = charset_size ** length
    attempts_per_second = 1e6  # Assuming 1 million attempts per second
    time_seconds = total_combinations / attempts_per_second

    return conversion(time_seconds)

# ==================================================================================================================================
    # 3. If more than 8 characters, calculate how long a potential brute force may take on it
        # (Try to make sure password contains a mix of uppercase, lowercase, numbers, and special characters. If it doesn't, the criteria is false)

def validate_password(password):
    if len(password) < 8:
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c.isprintable() and not c.isalnum() for c in password):
        return False
    return True

# ==================================================================================================================================
    # 3. Add an entropy calculator to show the mathematical strength of the password
def calculate_entropy(password):
    charset_size = 0
    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    # Determine special characters from the actual alphabet rather than assuming 32
    special_count = sum(1 for ch in ALPHABET if ch.isprintable() and not ch.isalnum())
    if any(c.isprintable() and not c.isalnum() for c in password):
        charset_size += special_count

    # Entropy (bits) = length * log2(charset_size)
    entropy = 0.0
    if charset_size > 0:
        entropy = len(password) * math.log2(charset_size)
    return entropy

# ==================================================================================================================================
    # 4. Based on the entropy, display a message to the user and let them know if the password is strong enough to be used
def password_strength(entropy):
    if entropy < 28:
        return "Very Weak\nConsider using a longer password with a mix of character types to increase strength."
    elif entropy < 36:
        return "Weak\nConsider using a longer password with a mix of character types to increase strength."
    elif entropy < 60:
        return "Reasonable"
    elif entropy < 128:
        return "Strong"
    else:
        return "Very Strong"
    
# ===============================================================================================================================
    # 5. Print all of the qualities of the password to the user, and give them the option to generate a new one if they are not satisfied with it
def main():
    while True:
        password = generate_password(length)
        print(f"Generated Password: {password}")
        
        if length < 8:
            print(f"Brute Force Simulation Time: {brute_force_demo(length)}")
        else:
            print(f"Brute Force Time Estimate: {brute_force_estimate(length)}")
        
        print(f"Password Entropy: {round(calculate_entropy(password), 2)} bits")
        print(f"Password Validation: {'Meets criteria' if validate_password(password) else 'Does not meet criteria'}")
        print(f"Password Strength: {password_strength(calculate_entropy(password))}")
        
        print("=============================================================================================================")
        choice = input("Do you want to generate a new password? (yes/no): ")
        print("=============================================================================================================")
        
        if choice.lower() != 'yes':
            print(f"Congratulations! Your password is: {password}")
            print("=============================================================================================================")
            break

# ==================================================================================================================================
    # Driver Code
if __name__ == "__main__":
    main()

# ==================================================================================================================================
