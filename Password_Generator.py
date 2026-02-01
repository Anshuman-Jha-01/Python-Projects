import random
import string

# Define the character set: letters, digits, and punctuation
characters = string.ascii_letters + string.digits + string.punctuation

# Ask user for password length
n = int(input("🔢 Enter the length of the password: "))

# Generate password using random choices
password = ""
i=1
while i<=n:
    password = password + random.choice(characters)
    i = i+1

# Display the password
print("✅ Generated Password:", password)