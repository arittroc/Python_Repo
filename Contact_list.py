list = {}

def start():
    print "Welcome to Contact+ \n \nPlease enter your name: ",
    name = raw_input()
    print "Hi " + name + " would you like to check your current contacts or make new ones? \nTo make new contacts type in 'New' \nTo check current contacts type in 'Contacts'"
    print "Go to: ",
    choose = ""
    choose = raw_input()
    valid = False
    while(not valid):
        if choose == "'New'" or choose == "'new'" or choose == "New" or choose == "new":
            new_function()
        elif choose == "'Contacts'" or choose == "'contacts'" or choose == "Contacts" or choose == "contacts":
            contacts_function()

def new_function():
    global list
    list = {}
    print "\nPlease input the name: ",
    contact_name = raw_input()
    print "Please input the number: ",
    contact_number = raw_input()
    list.update({contact_name:contact_number})
    print "Contact created \n\nWould you like to make more contacts or check current contacts? \nTo make new contacts type in 'New' \nTo check current contacts type in 'Contacts'"
    print "Go to: ",
    choose = ""
    choose = raw_input()
    valid = False
    while(not valid):
        if choose == "'New'" or choose == "'new'" or choose == "New" or choose == "new":
            new_function()
        elif choose == "'Contacts'" or choose == "'contacts'" or choose == "Contacts" or choose == "contacts":
            contacts_function()

def contacts_function():
    global list
    for keys,values in list.items():
        print "\n---------------------------------------------------------"
        print str("Name: ") + str(keys)
        print str("Number: ") + str(values)
        print "---------------------------------------------------------\n"
    print "Would you like to make more contacts or check current contacts? \nTo make new contacts type in 'New' \nTo check current contacts type in 'Contacts'"
    print "Go to: ",
    choose = ""
    choose = raw_input()
    valid = False
    while(not valid):
        if choose == "'New'" or choose == "'new'" or choose == "New" or choose == "new":
            new_function()
        elif choose == "'Contacts'" or choose == "'contacts'" or choose == "Contacts" or choose == "contacts":
            contacts_function()

start()