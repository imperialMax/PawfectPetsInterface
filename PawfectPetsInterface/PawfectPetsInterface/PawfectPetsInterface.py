import pyodbc
from argon2 import PasswordHasher
ph = PasswordHasher()
connection_string = (
    r"Driver={ODBC Driver 17 for SQL Server};"
    r"Server=LAPTOP-E8GVKM9S\SQLEXPRESS;"
    r"Database=ElysiumLuxuryDB;"
    r"Trusted_Connection=yes;"
    r"Column Encryption Setting=Enabled;"
    
)

global verifieduser 



verifieduser = False
def editSuppliers():
    supplierTransaction = input("Suppliers:" + "\n" +
                          "1. Select" + "\n" +
                          "2. Insert" + "\n" +
                          "3. Update" + "\n" +
                          "4. Delete" + "\n")
    match supplierTransaction:
        case "1":
            SelectSuppliers()
        case "2":
            InsertSuppliers()
        case "3":
            UpdateSuppliers()
        case "4":
            pass

def editProducts():
    productTransaction = input("Products:" + "\n" +
                          "1. Select" + "\n" +
                          "2. Insert" + "\n" +
                          "3. Update" + "\n" +
                          "4. Delete" + "\n")
    match productTransaction:
        case "1":
            SelectProducts()
        case "2":
            InsertProducts()
        case "3":
            pass
        case "4":
            pass

def editCustomers():
    customerTransaction = input("Customers:" + "\n" +
                          "1. Select" + "\n" +
                          "2. Insert" + "\n" +
                          "3. Update" + "\n" +
                          "4. Delete" + "\n")
    match customerTransaction:
        case "1":
            SelectCustomers()
        case "2":
            InsertCustomers()
        case "3":
            pass
        case "4":
            pass


### SUPPLIERS
def InsertSuppliers():
    supplierInput = input("What is the name of the supplier?" + "\n")
    contactInput = input("What is the contact email of the supplier?" + "\n") ### format the input somehow???? 


    conn = pyodbc.connect(connection_string)
    
    cursor = conn.cursor()
    
    insertQuery = """ INSERT INTO suppliers (supplier_name, supplier_email) VALUES (?,?) """ 
    
    data = (supplierInput, contactInput)

    cursor.execute(insertQuery,data)
    conn.commit()
    cursor.close()
    conn.close()

def SelectSuppliers():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    uInput = input("Would you like to view the entire table or just one row?" + "\n" + "Select an option by entering the corresponding number:"
                   + "\n" + "1. Entire table" + "\n" + "2. One row" + "\n")
    match uInput:
        case "1":
            select_Query = ''' 
                SELECT * FROM suppliers
            '''
            cursor.execute(select_Query)
            result = cursor.fetchall()
            resultList = [result]
            print("Here are the results of your search:" + "\n")
            print(resultList)
            print("\n")
        case "2":
            uInput = input("Which row would you like to view?" + "\n" + "Select an option by entering the corresponding number:"
                   + "\n" + "1. supplier_name" + "\n" + "2. supplier_email" + "\n")
            match uInput:
                case "1":
                    select_Query = ''' 
                        SELECT supplier_name FROM suppliers
                    '''
                    cursor.execute(select_Query)
                    result = cursor.fetchall()
                    resultList = [result]
                    print("Here are the results of your search:" + "\n")
                    print(resultList)
                    print("\n")
                case "2":
                    select_Query = ''' 
                        SELECT supplier_email FROM suppliers
                    '''
                    cursor.execute(select_Query)
                    result = cursor.fetchall()
                    resultList = [result]
                    print("Here are the results of your search:" + "\n")
                    print(resultList)
                    print("\n")
    cursor.close()
    conn.close()

def UpdateSuppliers():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    select_Query = ''' 
        SELECT * FROM suppliers     
    '''
    cursor.execute(select_Query)
    result = cursor.fetchall()
    resultList = [result]

    print("Here is the contents of the table:" + "\n")
    print(resultList)
    print(resultList)
    uInput = input("\n" + "What would you like to update?" + "\n" + "Select an option by entering the corresponding number:" 
          + "\n" + "1. supplier_name"
          + "\n" + "2. supplier_email" + "\n")
    supplier_ID = input("What is the ID of the supplier that you want to edit?"
          + "\n" + "Select an option by entering the number appearing at the front of the supplier's list:"
          + "\n")
    match uInput:
        case "1":
            updatedValue = input("The supplier_name is currently " + resultList[1] + "." 
                                 + "\n" + "What should the updated value be?" 
                                 + "\n")
            update_Query = """
                UPDATE suppliers SET supplier_name WHERE supplier_ID VALUES (?,?) 
            """

            data = (updatedValue,supplier_ID)

            cursor.execute(update_Query,data)
            conn.commit()
            cursor.close()
            conn.close()
### PRODUCTS
def InsertProducts():
    productInput = input("What is the name of the product?" + "\n")
    costInput = input("what is the cost of the product?" + "\n")
    supplierInput = input("what is the ID of the supplier?" + "\n")

    #######################################################
    #######################################################x`lookup supplier, produce list?? list must be names not keys

    conn = pyodbc.connect(connection_string)
    
    cursor = conn.cursor()
    
    insertQuery = """ INSERT INTO products (supplier_ID, product_name, product_cost) VALUES (?, ?, ?) """ 
    
    data = (supplierInput, 
            productInput, costInput)

    cursor.execute(insertQuery,data)
    conn.commit()
    cursor.close()
    conn.close()

def SelectProducts():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    uInput = input("Would you like to view the entire table or just one row?" + "\n" + "Select an option by entering the corresponding number:"
                   + "\n" + "1. Entire table" + "\n" + "2. One row" + "\n")
    match uInput:
        case "1":
            select_Query = ''' 
                SELECT * FROM products
            '''
            cursor.execute(select_Query)
            result = cursor.fetchall()
            resultList = [result]
            print("Here are the results of your search:" + "\n")
            print(resultList)
            print("\n")
        case "2":
            uInput = input("Which row would you like to view?" + "\n" + "Select an option by entering the corresponding number:"
                   + "\n" + "1. product_name" + "\n" + "2. product_cost" + "\n")
            match uInput:
                case "1":
                    select_Query = ''' 
                        SELECT product_name FROM products
                    '''
                    cursor.execute(select_Query)
                    result = cursor.fetchall()
                    resultList = [result]
                    print("Here are the results of your search:" + "\n")
                    print(resultList)
                    print("\n")
                case "2":
                    select_Query = ''' 
                        SELECT product_cost FROM products
                    '''
                    cursor.execute(select_Query)
                    result = cursor.fetchall()
                    resultList = [result]
                    print("Here are the results of your search:" + "\n")
                    print(resultList)
                    print("\n")
    cursor.close()
    conn.close()
### CUSTOMERS
def InsertCustomers():
    firstNameInput = input("What is the customer's first name?" + "\n")
    lastNameInput = input("What is the customer's last name?" + "\n")
    emailInput = input("What is the customer's email?" + "\n")
    addressInput = input("What is the customer's address?" + "\n")
    phoneNumberInput = input("What is the customer's phone number?" + "\n")


    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    insertQuery = """ INSERT INTO customers (first_name, last_name, email, address, phone_number) VALUES (?, ?, ?, ?, ?) """

    data = (firstNameInput, lastNameInput, emailInput, addressInput, phoneNumberInput)

    cursor.execute(insertQuery,data)
    conn.commit()
    cursor.close()
    conn.close()

def SelectCustomers():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    uInput = input("Would you like to view the entire table or just one row?" + "\n" + "Select an option by entering the corresponding number:"
                   + "\n" + "1. Entire table" + "\n" + "2. One row" + "\n")
    match uInput:
        case "1":
            select_Query = ''' 
                SELECT * FROM customers
            '''
            cursor.execute(select_Query)
            result = cursor.fetchall()
            resultList = [result]
            print("Here are the results of your search:" + "\n")
            print(resultList)
            print("\n")
        case "2":
            uInput = input("Which row would you like to view?" + "\n" + "Select an option by entering the corresponding number:"
                   + "\n" + "1. first_name" 
                   + "\n" + "2. last_name" 
                   + "\n" + "3. email"
                   + "\n" + "4. address"
                   + "\n" + "5. phone_number"
                   + "\n")
            match uInput:
                case "1":
                    select_Query = ''' 
                        SELECT first_name FROM customers
                    '''
                    cursor.execute(select_Query)
                    result = cursor.fetchall()
                    resultList = [result]
                    print("Here are the results of your search:" + "\n")
                    print(resultList)
                    print("\n")
                case "2":
                    select_Query = ''' 
                        SELECT last_name FROM customers
                    '''
                    cursor.execute(select_Query)
                    result = cursor.fetchall()
                    resultList = [result]
                    print("Here are the results of your search:" + "\n")
                    print(resultList)
                    print("\n")
                case "3":
                    select_Query = ''' 
                        SELECT email FROM customers
                    '''
                    cursor.execute(select_Query)
                    result = cursor.fetchall()
                    resultList = [result]
                    print("Here are the results of your search:" + "\n")
                    print(resultList)
                    print("\n")
                case "4":
                    select_Query = ''' 
                        SELECT address FROM customers
                    '''
                    cursor.execute(select_Query)
                    result = cursor.fetchall()
                    resultList = [result]
                    print("Here are the results of your search:" + "\n")
                    print(resultList)
                    print("\n")
                case "5":
                    select_Query = ''' 
                        SELECT phone_number FROM customers
                    '''
                    cursor.execute(select_Query)
                    result = cursor.fetchall()
                    resultList = [result]
                    print("Here are the results of your search:" + "\n")
                    print(resultList)
                    print("\n")



    cursor.close()
    conn.close()

def createUser():
    username = input("What will your username be?" + "\n")
    password = input("What will your password be?" + "\n")

    passwordHash = ph.hash(password)

    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    insertQuery = """ INSERT INTO administrators (username, password) VALUES (?,?) """

    data = (username, passwordHash)

    cursor.execute(insertQuery, data)
    conn.commit()
    cursor.close()
    conn.close()
    
def verifyUser():
    global verifieduser
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    try:
        username = input("What is your username?" + "\n")
        password = input("What is your password?" + "\n")

        select_query = '''
            SELECT password FROM administrators WHERE username = ?
        '''

        cursor.execute(select_query, (username,))
        result = cursor.fetchone()

        if result:
            password_hash = result[0]
            if ph.verify(password_hash, password):
                
                verifieduser = True
                
            else:
                print("password is incorrect")
        else:
            print("username not found")
    except Exception as e:
        print(f"An error occured: {e}")
    finally:
        cursor.close()


while True:
    if verifieduser == True:
        break
    else:

        loginOrCreateAccount = input("Do you wish to login or create an account?" + "\n" + 
                                 "Please select an option by entering the corresponding number:" + "\n" +
                                 "1. Login" + "\n" +
                                 "2. Create Account" + "\n")

        match loginOrCreateAccount:
            case "1":
                
                verifyUser()
            case "2":
                createUser()
                createdaccount = True



while True:

    uInput = input("Welcome to the Pawfect Pets database" + "\n" +
                       "Please select an option by entering the corresponding number" + "\n" + 
                       "1. Edit Products" + "\n" +
                       "2. Edit Suppliers" + "\n" +
                       "3. Edit Customers" + "\n")
    match uInput:
        case "1":
            editProducts()
        case "2":
            editSuppliers()
        case "3":
            editCustomers()



