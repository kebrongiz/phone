def mobile_or_not():
    phone_number = input("Enter the number:")
    while len(phone_number) != 9:
         print("please Enter the 9 digit number.")
         phone_number = input("Enter the number:")
    if phone_number[0] == "9":
         print("Mobile")
    else:
         print("fixed phone")
    return

print(mobile_or_not())






