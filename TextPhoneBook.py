def main():

    import sqlite3

    def add_contact():
        fname = input('First name: ')
        lname = input('Last name: ')
        phone_number = input('Phone number : ')
        email = input('E-mail address: ')

        cursor.execute('''
        INSERT INTO Contacts ("first_name", "last_name", "phone_number", "email")
        VALUES (?, ?, ?, ?);
        ''', (fname, lname, phone_number, email))

        connection.commit()
        print('\nData added successfully.')

    def show_contacts():
        
        cursor.execute('''
        SELECT * FROM "Contacts"
        ''')

        rows = cursor.fetchall()
        for row in rows:
            print("{0}. {1} {2}; TEL.: {3}; E-MAIL: {4}".format(row[0], row[1], row[2], row[3], row[4]))
    
    def select_contact():
        print('State the ID number of the contact you wish to select.')
        id_input = input('> ')

        while id_input.isnumeric() != True:
            print('Incorrect input. Try again.')
            id_input = input('> ')
        
        cursor.execute('''
        SELECT * FROM Contacts WHERE id = ?
        ''', (id_input))
        
        row = cursor.fetchone()
        print("Selected entry: {0}. {1} {2}; TEL.: {3}; E-MAIL: {4}".format(row[0], row[1], row[2], row[3], row[4]))
        return id_input

    def edit_contact():

        show_contacts()

        id_input = select_contact()
        
        print('What would you like to edit? (select one)')
        is_correct = False

        while is_correct == False:

            what_to_edit = input('> ')
            availible_options = ('first name', 'surname', 'last name', 'phone', 'tel', 'telephone', 'phone number', 'email', 'mail', 'e-mail')

            if what_to_edit in availible_options:
                is_correct = True

        print('What is the new value?')
        new_value = input('> ')

        if what_to_edit.lower() == 'first name':
            cursor.execute('''UPDATE "Contacts" SET "first_name" = ? WHERE "id" = ?''', (new_value, id_input))

        elif what_to_edit.lower() == 'last name' or what_to_edit.lower() == 'surname':
            cursor.execute('''UPDATE "Contacts" SET "last_name" = ? WHERE "id" = ?''', (new_value, id_input))
        
        elif what_to_edit.lower() == 'phone' or what_to_edit.lower() == 'phone number' or what_to_edit.lower() == 'telephone' or what_to_edit.lower() == 'tel':
            cursor.execute('''UPDATE "Contacts" SET "phone_number" = ? WHERE "id" = ?''', (new_value, id_input))
       
        elif what_to_edit.lower() == 'email' or what_to_edit.lower() == 'e-mail' or what_to_edit.lower() == 'mail':
            cursor.execute('''UPDATE "Contacts" SET "email" = ? WHERE "id" = ?''', (new_value, id_input))
        
        connection.commit()
        print('Operation successful.')

        cursor.execute('''
        SELECT * FROM Contacts WHERE id = ?;
        ''', (id_input))
        
        row = cursor.fetchone()
        print("\nNew entry: {0}. {1} {2}; TEL.: {3}; E-MAIL: {4}".format(row[0], row[1], row[2], row[3], row[4]))

    def delete_contact():

        show_contacts()

        id_input = select_contact()
       
        cursor.execute('''DELETE FROM "Contacts" WHERE "id" = ?''', (id_input))
        
        connection.commit()
        print('Operation successful.')
    
    def help():
        print('''
    ===  HELP  ===
Add - adds new contact
Show - shows stored contacts
Edit - allows edition of a contact
Delete - allow deletion of a contact
Exit - leaves the programm
Help - shows help''') 

    try:
        connection = sqlite3.connect('textphonebook.db')
        cursor = connection.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Contacts
        ("id" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        "first_name" TEXT, "last_name" TEXT,
        "phone_number" INTEGER, "email" TEXT);
        ''')    

        usr_input = 'blank'
        
        print('''
==================================================================================================

 TTTTTT EEEEEE XXX XX TTTTTT    PPPPPP HH  HH  OOOO  NNN NN EEEEEE    BBBBB  OOOO   OOOO  KK KKK
   TT   EEE      XX     TT      PPPPPP HHHHHH OO  OO NN NNN EEE       BBBB  OO  OO OO  OO KKKK
   TT   EEEEEE XXX XX   TT      PPP    HH  HH  OOOO  NN  NN EEEEEE    BBBBB  OOOO   OOOO  KK KKK

==================================================================================================
BY defoxicator
        ''')

        commands = {
            'add': add_contact,
            'show': show_contacts,
            'edit': edit_contact,
            'delete': delete_contact,
            'help': help,
            }

        while usr_input != 'exit':
            print("\nType 'help' and press ENTER to see availible options.")
            usr_input = input("> ").lower()

#             if usr_input.lower() == 'add':
#                 add_contact()

#             if usr_input.lower() == 'show':
#                 show_contacts()
            
#             if usr_input.lower() == 'edit':
#                 edit_contact()
            
#             if usr_input.lower() == 'delete':
#                 delete_contact()

#             if usr_input.lower() == 'help':
#                 print('''
#     ===  HELP  ===
# Add - adds new contact
# Show - shows stored contacts
# Edit - allows edition of a contact
# Delete - allow deletion of a contact
# Exit - leaves the programm
# Help - shows help''')
    
            if usr_input in commands:
                commands[usr_input.lower()]()

    except sqlite3.error as e:
        print('\nOperation on database failed.', e)

    finally:
        print('\nThe application will now shut down.\n')
        cursor.close()
        connection.close()
        exit()

if __name__ == '__main__':
    main()