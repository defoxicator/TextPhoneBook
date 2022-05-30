def main():

    import sqlite3

    connection = sqlite3.connect('textphonebook.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Contacts
    ("id" INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    "first_name" TEXT, "last_name" TEXT,
    "phone_number" INTEGER, "email" TEXT);
    ''')

    def add_contact():
        fname = input('First name: ')
        lname = input('Last name: ')
        phone_number = input('Phone number :')
        email = input('E-mail address: ')

        cursor.execute('''
        INSERT INTO Contacts ("first_name", "last_name", "phone_number", "email")
VALUES ("{fname}", "{lname}", "{phone_number}", "{email}");
        ''')

        connection.commit()

    usr_input = 'blank'
    print("Type 'help' and press ENTER to see availible options.")
    while usr_input.lower() != 'exit':
        usr_input = input("> ")
        
        if usr_input.lower() == 'add':
            add_contact()

        if usr_input.lower() == 'help':
            print('''   ===  HELP  ===

Add - adds new contact
Exit - leaves the programm
Help - shows help
''')

if __name__ == '__main__':
    main()