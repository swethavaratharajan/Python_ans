import phonenumbers
my_string_number =input("Enter the Number: ")
my_number = phonenumbers.parse(my_string_number)
print(phonenumbers.is_possible_number(my_number))