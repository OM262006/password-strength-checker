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

    if char.isupper():
        has_uppercase = True

    start_with_letter = password[0].isupper() if length > 0 else False

if length >= 8 and has_numbers and has_spcial and has_uppercase and start_with_letter:
    print("strong")
else:
    print("weak")
