# R07-2FA06-CAHANAP.py

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
section_name = input("Enter your section: ")
favorite_subject = input("Enter your favorite subject: ")

full_name = first_name + "" + last_name

print("Name: ", first_name.capitalize(), last_name.capitalize())
print("Name Code: ", first_name.upper(), last_name.upper())
print("Section: ", section_name.upper())
print("Favorite Subject: ", favorite_subject.title())
print("Character Count: ", len(full_name))
