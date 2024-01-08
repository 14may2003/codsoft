import random
import string

def generate_password(length):
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Use random.choices() to generate a password with the specified length
    password = ''.join(random.choices(characters, k=length))

    return password

# Get the desired length of the password from the user
password_length = int(input("Enter the length of the password: "))

# Generate the password
generated_password = generate_password(password_length)

# Display the generated password
print("Generated Password:", generated_password)
