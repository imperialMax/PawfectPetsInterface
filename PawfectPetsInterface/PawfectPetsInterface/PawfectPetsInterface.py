import pyodbc
from argon2 import PasswordHasher
ph = PasswordHasher()
connection_string = (
    r"Driver={ODBC Driver 17 for SQL Server};"
    r"Server=LAPTOP-E8GVKM9S\SQLEXPRESS;"
    r"Database=VideogamesDB;"
    r"Trusted_Connection=yes;"
    r"Column Encryption Setting=Enabled;"
    
)

def InsertSuppliers():
    supplierInput = input("what is the name of the developer ")

    conn = pyodbc.connect(connection_string)
    
    cursor = conn.cursor()
    
    insertQuery = """ INSERT INTO developer (designer_name) VALUES (?) """ 
    
    data = (designerInput)

    cursor.execute(insertQuery,data)
    conn.commit()
    cursor.close()
    conn.close()

def InsertGame():
    gameNameInput = input("what is the name of the game ")
    genreInput = input("what is the genre of the game ")
    releaseDateInput = input("what was the release date of the game YYYY-MM-dd ")
    costInput = input("what was the cost of the game ")
    platformInput = input("what platform did the game release on ")

    conn = pyodbc.connect(connection_string)
    
    cursor = conn.cursor()
    
    insertQuery = """ INSERT INTO game (game_name, genre, date_of_release, cost, game_platform) VALUES (?, ?, ?, ?, ?) """ 
    
    data = (gameNameInput, genreInput, releaseDateInput, costInput, platformInput)

    cursor.execute(insertQuery,data)
    conn.commit()
    cursor.close()
    conn.close()

def InsertConsoles():
    designerInput = input("who designed console ")
    releaseDateInput = input("when was it released? YYYY-MM-dd ")
    priceInput = input("how much does it cost ")

    conn = pyodbc.connect(connection_string)
    
    cursor = conn.cursor()
    
    insertQuery = """ INSERT INTO console (designer, date_of_release, price) VALUES (?, ?, ?) """ 
    
    data = (designerInput,releaseDateInput,priceInput)

    cursor.execute(insertQuery,data)
    conn.commit()
    cursor.close()
    conn.close()

def InsertDevelopers():
    developerInput = input("what is the name of the developer ")
    countryInput = input("what country is the developer from ")

    conn = pyodbc.connect(connection_string)
    
    cursor = conn.cursor()
    
    insertQuery = """ INSERT INTO developer (dev_name, dev_country) VALUES (?, ?) """ 
    
    data = (developerInput, countryInput)

    cursor.execute(insertQuery,data)
    conn.commit()
    cursor.close()
    conn.close()

def InsertCustomers():
    usernameInput = input("Enter Username ")
    emailInput = input("Enter Email ")
    passwordOrigin = input("Enter Password ")
    fullNameInput = input("Enter Full Name (First and last name) ")
    phoneNumberInput = input("Enter phone number ")

    passwordHash = ph.hash(passwordOrigin)
    print(passwordHash)
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    insertQuery = """ INSERT INTO users (username, email, password, full_name, phone_number) VALUES (?, ?, ?, ?, ?) """

    data = (usernameInput, emailInput, passwordHash, fullNameInput, phoneNumberInput)

    cursor.execute(insertQuery,data)
    conn.commit()
    cursor.close()
    conn.close()
##deletions


def verifyUser():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    try:
        username = input("Enter username: ")
        password = input("Enter password: ")

        select_query = '''
            SELECT password_hash FROM users WHERE username = ?
        '''

        cursor.execute(select_query, (username,))
        result = cursor.fetchone()

        if result:
            password_hash = result[0]
            if ph.verify(password_hash, password):
                print("password is correct")
            else:
                print("password is incorrect")
        else:
            print("username not found")
    except Exception as e:
        print(f"An error occured: {e}")
    finally:
        cursor.close()


uInput = input("Welcome to the Videogames Database" + "\n" +
               "Please Select an option" + "\n" + 
               "1. Insert user" + "\n" +
               "2. Insert developer" + "\n" +
               "3. Insert game" + "\n" +
               "4. Insert console" + "\n" +
               "5. Insert designer" + "\n" +
               "6. Verify user" + "\n")
match uInput:
    case "1":
        InsertUsers()
    case "2":
        InsertDevelopers()
    case "3":
        InsertGame()
    case "4":
        InsertConsoles()
    case "5":
        InsertDesigners()
    case "6":
        verifyUser()
