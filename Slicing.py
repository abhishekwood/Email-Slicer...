print("!!! Welcome To Email Slicer !!!")

email = input("Enter Your E-Mail ID :- ").strip()

at_index = email.find('@')

if at_index > 0 and email.count('@') == 1:
    
    username = email[:at_index]
    domain = email[at_index + 1:]
    
    print(f"Username of Email is: {username}")
    
    if "." in domain and domain.find('.') > 0 and not domain.endswith('.'):
        print(f"Domain of Email is: {domain}")
    else:
        print("This looks like an invalid domain.\nPublic domains must contain a '.' (e.g., 'example.com').")

else:
    print("Invalid email address format.\nPlease make sure you enter a valid email.")
