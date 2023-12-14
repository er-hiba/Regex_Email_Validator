import re

def verify_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    regex = re.compile(pattern)
    
    if re.search(regex, email):
        return True
    else:
        return False


# Get user input for email address
email = input("Enter an email address to verify: ")

# Verify the email and display the result
if verify_email(email):
    print(f"The email '{email}' is valid.")
else:
    print(f"The email '{email}' is not valid.")
