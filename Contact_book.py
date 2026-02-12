'''
save contact in empty dictonary.

7 choice in Coontact book
1 = create contact
2 = view contact
3 = delete contact
4 = Update contact
5 = count contacts
6 = views all contacts
7 = Exit Book 

input choice
if elif else condition.
'''
contacts = {}

while True:
    print("1 - Create contact")
    print("2 - search contact")
    print("3 - Delete contact")
    print("4 - Update contact")
    print("5 - Count contacts")
    print("6 - view contacts")
    print("7 - Exit contact Book")

    user_choose = int(input("Enter your choice ="))

# 1-- create contact.

    if user_choose == 1:
        name = input("Enter contact name =")
        if name in contacts:
            print(f"Contact name {name} is already in contact book.")
        else:
            age = int(input("Enter your Age ="))
            Number = input("Enter your Mobile Number =")
            contacts[name] = {"Name" : name , "Age" : age ,"Number" : Number}
            print(f"contact name {name} has been created successfully")

# 2-- Search contact.

    elif user_choose == 2:
        name = input("Enter contact name to view =")
        if name in contacts:
            contact = contacts[name]
            print(f"Name : {contact["Name"]}, Age : {contact["Age"]}, Mobile Number : {contact["Number"]}")
        else:
            print("Contact not found!")


# 3-- Delete contact.
 
    elif user_choose == 3:
        name = input("Enter contact name to delete =")
        if name in contacts:
            del contacts[name]
            print(f"Contact name {name} has been deleted successfully")
        else:
            print("Contact not found!")


# 4-- Update contacts

    elif user_choose == 4:
        name = input("Enter contact name to update =")
        if name in contacts:
            age = int(input("Enter updated age ="))
            Number = int(input("Enter updated number ="))
            contacts[name]["Age"] = age
            contacts[name]["Number"] = Number
            print(f"Contact name {name} updated successfully")
        else:
            print("Contact not found")


# 5-- Counts contacts.

    elif user_choose == 5:
        print(f"{len(contacts)} contacts are in contact book")


# 6-- view contacts.

    elif user_choose == 6:
        print(f"View contacts in contact book -\n{contacts}")


# 7-- Exit Contact book.
            
    elif user_choose == 7:
        print("Good byyy.....\nThanks for using Contact book")
        break
    else:
        print("Invalid Input")