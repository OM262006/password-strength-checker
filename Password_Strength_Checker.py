password = input("ENTER YOUR PASSWORD:")

length = len(password)
has_numbers = False
has_spcial = False
has_uppercase = False

spcial_chars = "!@#$%^&*()_+-=| {}[]<>?,./;'"

for char in password:
    if char.isdigit():
        has_numbers = True
    
    if char in spcial_chars:
        has_spcial = True

    

if length >= 8 and has_numbers and has_spcial:
    print("strong")
else:
    print("weak")
